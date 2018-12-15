from flask import Blueprint, render_template, request

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
@blue.route('/user-list/',methods=['GET','POST'])
def user_list():
    users = User.query.filter_by(key=True)
    if request.method=="GET":
        return render_template('./user-list.html',users=users)
    if request.method=="POST":
        user=request.form.get('username')
        print(user)
        person=[]
        for i in users:
            if str(i.id)==user or i.username==user:
                person.append(i)
        if person:
            print(person[0].username)

            return render_template('./select-user.html',person=person[0])
        else:
            data={
                "id":"未查询到此用户",
                "username":"null",
                "email":"null",
                "address":'null',
                "time":"null",
            }
            return render_template('./select-user.html',person=data)



#已删除用户
@blue.route('/user-del/',methods=['GET',])
def user_del():
    users = User.query.filter_by(key=False)
    return render_template('./user-del.html',users=users)

#邮件模版
@blue.route('/email-model/',methods=['GET',])
def email_model():
    return render_template('./email_model.html')

#收件人列表编辑
@blue.route('/user-list/user-edit.html',methods=['GET',])
def user_edit():
    return render_template('./user-edit.html')

#增加用户弹框
@blue.route('/user-list/user-add.html',methods=['GET',])
def user_add():
    return render_template('./user-add.html')

#查询到的用户
@blue.route('/select-user/',methods=['GET',])
def select_user():

    user=request.form.get()
    if request.method=='GET':

        return render_template('./select-user.html',user=user)





#测试接口
@blue.route('/test/')
def test11():
    names=User.query.all()
    hehe=names[0].key


    print(hehe)

    return render_template('./1111111.html',names=names)






















