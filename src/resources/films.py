import datetime
from flask_restful import Resource

from flask import request
from marshmallow import ValidationError
from sqlalchemy.orm import joinedload

from src import db
from src.database.models import Film
from src.resources.auth import token_required
from src.schemas.films import FilmSchema
from src.services.film_service import FilmService


class FilmListApi(Resource):
    film_schema = FilmSchema()

    @token_required
    def get(self, uuid=None):
        if not uuid:
            films = FilmService.fetch_all_films(db.session).options(
                joinedload(Film.actors)
            ).all()
            return self.film_schema.dump(films, many=True), 200
        film = FilmService.fetch_film_by_uuid(db.session, uuid)
        if not film:
            return f'Sorry, but film with id: {uuid} not found', 404
        return self.film_schema.dump(film), 200

    @token_required
    def post(self):
        try:
            film = self.film_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(film)
        db.session.commit()
        return self.film_schema.dump(film), 201

    @token_required
    def put(self, uuid=None):
        film = FilmService.fetch_film_by_uuid(db.session, uuid)
        if not film:
            return "", 404
        try:
            film = self.film_schema.load(request.json, instance=film, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(film)
        db.session.commit()
        return self.film_schema.dump(film), 200

    # TODO: added Marshmallow validations
    @token_required
    def patch(self, uuid=None):
        if not uuid:
            return {'message': 'Please send id film'}, 400
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return {'message': f'Sorry, but film with id {uuid} not found'}, 404
        film_json = request.json
        if not film_json:
            return {'message': 'Request data is empty'}, 400
        title = film_json.get('title')
        release_date = datetime.datetime.strptime(film_json.get('release_date'), '%B %d, %Y') if film_json.get(
            'release_date') else None
        distributed_by = film_json.get('distributed_by')
        rating = film_json.get('rating')
        length = film_json.get('length')
        description = film_json.get('description')
        if title:
            film.title = title
        elif release_date:
            film.release_date = release_date
        elif distributed_by:
            film.distributed_by = distributed_by
        elif rating:
            film.rating = rating
        elif length:
            film.length = length
        elif description:
            film.description = description

        db.session.add(film)
        db.session.commit()
        return {'message': f'Film with id: {uuid} updated successfully'}, 200

    @token_required
    def delete(self, uuid=None):
        if not uuid:
            return {'message': 'Please send id film'}, 400
        film = FilmService.fetch_film_by_uuid(db.session, uuid)
        if not film:
            return f'Sorry, but film with id {uuid} not found', 404
        db.session.delete(film)
        db.session.commit()
        return f'Film with id {uuid} deleted successfully', 204
