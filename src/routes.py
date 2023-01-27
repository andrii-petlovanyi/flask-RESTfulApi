from src import api
from src.resources.actors import ActorListApi
from src.resources.aggregations import AggregationsApi
from src.resources.auth import AuthRegister, AuthLogin
from src.resources.films import FilmListApi
from src.resources.hello import Hello
from src.resources.populate_db import PopulateDB, PopulateDBThreadPoolExecutor

api.add_resource(Hello, '/')
api.add_resource(FilmListApi, '/films', '/films/<uuid>', strict_slashes=False)
api.add_resource(ActorListApi, '/actors', '/actors/<id>', strict_slashes=False)
api.add_resource(AggregationsApi, '/aggregations', strict_slashes=False)
api.add_resource(AuthRegister, '/register', strict_slashes=False)
api.add_resource(AuthLogin, '/login', strict_slashes=False)
api.add_resource(PopulateDB, '/populate_db', strict_slashes=False)
api.add_resource(PopulateDBThreadPoolExecutor, '/populate_db_ex', strict_slashes=False)
