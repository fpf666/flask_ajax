from flask_restful import Api

from App.apis import Base, Regist, Login, Update

api = Api()

api.add_resource(Base,'/base/')
api.add_resource(Regist,'/regist/')
api.add_resource(Login,'/login/')
api.add_resource(Update,'/update/')


def init_api(app):
    api.init_app(app=app)