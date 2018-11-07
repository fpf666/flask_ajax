

def data_uri(data):
    dialect = data.get('dialect')
    driver  = data.get('driver')
    user = data.get('user')
    password =data.get('password')
    host = data.get('host')
    port = data.get('port')
    database = data.get('database')
    return '{}+{}://{}:{}@{}:{}/{}'.format(dialect,driver,user,password,host,port,database)



class Config():
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '110'



class DevelopConfig(Config):
    data = {
        'dialect': 'mysql',
        'driver':'pymysql',
        'user': 'root',
        'password':'964351153',
        'host':'localhost',
        'port':'3306',
        'database':'flask3',
    }

    SQLALCHEMY_DATABASE_URI = data_uri(data)


env = {
    'develop': DevelopConfig
}