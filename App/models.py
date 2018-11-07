
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_sql(app):
    db.init_app(app=app)



class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),unique=True)
    password = db.Column(db.String(64))
    age = db.Column(db.Integer,default=18)
    sex = db.Column(db.Integer,default=1)

    def to_dict(self):
        return {'name':self.name,'id':self.id,'age':self.age,'sex':self.sex}
