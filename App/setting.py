# 服务器连接
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
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '110'



class DevelopConfig(Config):
    data = {
        'dialect': 'mysql',
        'driver':'pymysql',
        'user': 'root',
        'password':'12345678',
        'host':'localhost',
        'port':'3306',
        'database':'email',
    }

    SQLALCHEMY_DATABASE_URI = data_uri(data)


env = {
    'develop': DevelopConfig
}