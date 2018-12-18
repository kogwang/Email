from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#连接数据库
def init_sql(app):
    db.init_app(app=app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(20),unique=True)
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    time = db.Column(db.String(100))
    key = db.Column(db.Boolean,default=True)


# 邮件模版表
class Models(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    model_name = db.Column(db.String(20))
    msg = db.Column(db.String(1000),default='模版未编辑')
    last_date=db.Column(db.String(100))
    last_time = db.Column(db.String(100))
    jishi=db.Column(db.Boolean,default=False)
    count=db.Column(db.String(100))
    key = db.Column(db.Boolean, default=True)
