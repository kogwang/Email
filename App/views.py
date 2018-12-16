import time

from flask import Blueprint, render_template, request

from App.models import User, db

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
def user_list(page=None):
    # print(page)

    if page=='1':
        return '1111'



    users = User.query.filter_by(key=True)
    if request.method=="GET":
        num=0
        for i in users:
            num+=1
        data={
            'users':users,
            'num':num
        }
        return render_template('./user-list.html',data=data)
    if request.method=="POST":
        user=request.form.get('username')
        # print(user)
        person=[]
        for i in users:
            if str(i.id)==user or i.username==user:
                person.append(i)
        if person:
            # print(person[0].username)
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
            # return '未查询到此用户'


#已删除用户
@blue.route('/user-del/',methods=['GET',])
def user_del():
    users = User.query.filter_by(key=False)
    if request.method=="GET":
        num=0
        for i in users:
            num+=1
        data={
            'users':users,
            'num':num
        }
    return render_template('./user-del.html',data=data)

#邮件模版
@blue.route('/email-model/',methods=['GET',])
def email_model():
    return render_template('./email_model.html')

#收件人列表编辑
@blue.route('/user-list/user-edit.html',methods=['GET',"POST"])
def user_edit():
    if request.method=='GET':
        return render_template('./user-edit.html')
    if request.method=="POST":
        username=request.form.get('username')
        email=request.form.get('email')
        address=request.form.get('address')

        id = request.form.get('id')
        user=User.query.filter_by(id=id)
        for i in user:
            if i.id==id:
                # 此时user对象就是要修改的用户 执行以下代码
                pass


        if username:
            if address:
                print(username, email, address)
                return '全写了'
            else:
                print(username, email, address)
                return '写了 useranme email'
        if address:
            print(username, email, address)
            return '写了 address email'

        print(username, email, address)

        return '只有email'


#增加用户弹框
@blue.route('/user-list/user-add.html',methods=['GET',"POST"])
def user_add():
    if request.method=="GET":
        return render_template('./user-add.html')
    if request.method=="POST":
        user = User()
        username=request.form.get('username')
        sql_user=User.query.filter_by(username=username)
        for i in sql_user:
            if i.username==username:
                return '数据库已存在该用户'
            # s_name=sql_user[0].username
            # print(s_name)
            # if username==s_name:
            #     return '数据库已存在该用户'
        email=request.form.get('email')
        address=request.form.get('address')
        user.username=username
        user.email=email
        user.address=address
        t = time.localtime()
        T = "{}:{}:{}".format(t.tm_hour, t.tm_min, t.tm_sec)
        user.time=T
        user.key=1
        db.session.add(user)
        db.session.commit()
        return '添加成功'

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






















