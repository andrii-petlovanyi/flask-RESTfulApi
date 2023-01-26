from src import api
from src.resources.actors import ActorListApi
from src.resources.films import FilmListApi
from src.resources.hello import Hello

api.add_resource(Hello, '/')
api.add_resource(FilmListApi, '/films', '/films/<uuid>', strict_slashes=False)
api.add_resource(ActorListApi, '/actors', '/actors/<id>', strict_slashes=False)
