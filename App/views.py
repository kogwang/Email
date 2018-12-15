from flask import Blueprint, render_template

blue = Blueprint('email',__name__)

#登录界面
@blue.route('/')
def login():
    return render_template('./login.html')

#index网页
@blue.route('/index/')
def index():
    return render_template('./index.html')

#右侧统计内容
@blue.route('/welcome/')
def welcome():
    return render_template('./welcome.html')

#用户列表
@blue.route('/user-list/')
def user_list():
    return render_template('./user-list.html')

#已删除用户
@blue.route('/user-del/')
def user_del():
    return render_template('./user-del.html')

#邮件模版
@blue.route('/email-model/')
def email_model():
    return render_template('./email_model.html')

#收件人列表编辑
@blue.route('/user-list/user-edit.html')
def user_edit():
    return render_template('./user-edit.html')

