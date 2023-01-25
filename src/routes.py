import datetime
from flask import request
from flask_restful import Resource

from src import api, db
from src.models import Film


class FilmListApi(Resource):
    def get(self, uuid=None):
        if not uuid:
            films = db.session.query(Film).all()
            return [f.to_dict() for f in films], 200
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return f'Sorry, but film with id: {uuid} not found', 404
        return film.to_dict(), 200

    def post(self):
        film_json = request.json
        if not film_json:
            return {'message': 'Request data is empty'}, 400
        try:
            film = Film(
                title=film_json['title'],
                release_date=datetime.datetime.strptime(film_json['release_date'], '%B %d, %Y'),
                distributed_by=film_json['distributed_by'],
                rating=film_json.get('rating'),
                length=film_json.get('length'),
                description=film_json.get('description')
            )
            db.session.add(film)
            db.session.commit()
        except (ValueError, KeyError):
            return {'message': 'Wrong request data'}, 400
        return {'message': 'Film added successfully', 'uuid': film.uuid}, 201

    def put(self, uuid=None):
        if not uuid:
            return {'message': 'Please send id film'}, 400
        film_json = request.json
        if not film_json:
            return {'message': 'Request data is empty'}, 400
        try:
            db.session.query(Film).filter_by(uuid=uuid).update(
                dict(
                    title=film_json['title'],
                    release_date=datetime.datetime.strptime(film_json['release_date'], '%B %d, %Y'),
                    distributed_by=film_json['distributed_by'],
                    rating=film_json.get('rating'),
                    length=film_json.get('length'),
                    description=film_json.get('description')
                )
            )
            db.session.commit()
        except (ValueError, KeyError):
            return {'message': 'Wrong request data'}, 400
        return {'message': f'Film with id: {uuid} updated successfully'}, 200

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

    def delete(self, uuid=None):
        if not uuid:
            return {'message': 'Please send id film'}, 400
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return f'Sorry, but film with id {uuid} not found', 404
        db.session.delete(film)
        db.session.commit()
        return f'Film with id {uuid} deleted successfully', 204


class Hello(Resource):
    def get(self):
        return {'message': 'Hello, Andrii'}, 200


api.add_resource(Hello, '/')
api.add_resource(FilmListApi, '/films', '/films/<uuid>', strict_slashes=False)
