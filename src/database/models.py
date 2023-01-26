import uuid

from src import db

movies_actors = db.Table(
    'movies_actors',
    db.Column('actor_id', db.Integer, db.ForeignKey('actors.id')),
    db.Column('film_id', db.Integer, db.ForeignKey('films.id'))
)


class Film(db.Model):
    __tablename__ = 'films'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    release_date = db.Column(db.Date, index=True, nullable=False)
    uuid = db.Column(db.String(36), unique=True)
    description = db.Column(db.Text)
    distributed_by = db.Column(db.String(128), nullable=False)
    length = db.Column(db.Float)
    rating = db.Column(db.Float)
    actors = db.relationship('Actor', secondary=movies_actors, lazy=True, backref=db.backref('films', lazy=True))

    def __init__(self, title, release_date, description, distributed_by, length, rating, actors=None):
        self.title = title
        self.release_date = release_date
        self.uuid = str(uuid.uuid4())
        self.description = description
        self.distributed_by = distributed_by
        self.length = length
        self.rating = rating
        if not actors:
            self.actors = []
        else:
            self.actors = actors

    def __repr__(self):
        return f'Film({self.title}, {self.release_date}, {self.uuid}, {self.distributed_by}, {self.rating}, {self.actors}'


class Actor(db.Model):
    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    birthday = db.Column(db.Date)
    is_active = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'Actor({self.name}, {self.birthday})'


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __init__(self, username, email, password):
        self.uuid = str(uuid.uuid4())
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f'Actor({self.name}, {self.birthday}, {self.uuid}, {self.is_active})'
