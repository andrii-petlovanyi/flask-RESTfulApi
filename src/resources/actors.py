import datetime
from flask_restful import Resource

from flask import request
from marshmallow import ValidationError

from src import db
from src.database.models import Actor
from src.schemas.actors import ActorSchema


class ActorListApi(Resource):
    actor_schema = ActorSchema()

    def get(self, id=None):
        if not id:
            actors = db.session.query(Actor).all()
            return self.actor_schema.dump(actors, many=True), 200
        actor = db.session.query(Actor).filter_by(id=id).first()
        if not actor:
            return f'Sorry, but actor with id: {id} not found', 404
        return self.actor_schema.dump(actor), 200

    def post(self):
        try:
            actor = self.actor_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(actor)
        db.session.commit()
        return self.actor_schema.dump(actor), 201

    def put(self, id):
        actor = db.session.query(Actor).filter_by(id=id).first()
        if not actor:
            return {'message': f'Sorry, but user with id {id} not found'}, 404
        try:
            actor = self.actor_schema.load(request.json, instance=actor, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(actor)
        db.session.commit()
        return self.actor_schema.dump(actor), 200

    def delete(self, id):
        if not id:
            return {'message': 'Please send id actor'}, 400
        actor = db.session.query(Actor).filter_by(id=id).first()
        if not actor:
            return f'Sorry, but actor with id {id} not found', 404
        db.session.delete(actor)
        db.session.commit()
        return f'Actor with id {id} deleted successfully', 204
