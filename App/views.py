from flask import Blueprint, render_template, jsonify

from App.models import User

blue = Blueprint('email',__name__)

#登录界面
@blue.route('/',methods=['GET',])
def login():
    return render_template('./login.html')

#index网页
@blue.route('/index/',methods=['GET',])
def index():
    return render_template('./index.html')

#右侧统计内容
@blue.route('/welcome/',methods=['GET',])
def welcome():
    return render_template('./welcome.html')

#用户列表
@blue.route('/user-list/',methods=['GET',])
def user_list():
    return render_template('./user-list.html')

#已删除用户
@blue.route('/user-del/',methods=['GET',])
def user_del():
    return render_template('./user-del.html')

#邮件模版
@blue.route('/email-model/',methods=['GET',])
def email_model():
    return render_template('./email_model.html')

#收件人列表编辑
@blue.route('/user-list/user-edit.html',methods=['GET',])
def user_edit():
    return render_template('./user-edit.html')

#测试接口
@blue.route('/test/')
def test11():
    user_names=User.query.all()
    data={
        'usernames':user_names
    }
    return render_template('./1111111.html',user_names=user_names)






















