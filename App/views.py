import json
import smtplib
import time
from email.mime.text import MIMEText

from flask import Blueprint, render_template, request
from flask.json import jsonify

from App.models import User, db, Models

blue = Blueprint('email',__name__)

#
# #登录界面
# @blue.route('/',methods=['GET',])
# def login():
#     return render_template('./login.html')


#登录界面
@blue.route('/',methods=['GET',"POST"])
def login():
    if request.method=="POST":
        if request.form.get('username')!='admin':
            return render_template('./login.html')
        if request.form.get('password')!='123456':
            return render_template('./login.html')
        return render_template('./index.html')
    if request.method=='GET':
        return render_template('./login.html')



#index网页
@blue.route('/index/',methods=['GET',])
def index():
    return render_template('./index.html')

#右侧统计内容
@blue.route('/welcome/',methods=['GET',])
def welcome():
    models=Models.query.filter_by(key=1)
    return render_template('./welcome.html',models=models)

#逻辑删除用户
@blue.route('/delUser/',methods=['POST'])
def delUser():
    user_id = json.loads(request.form.get('data'))
    for userid in user_id['id']:
        user = User.query.filter(User.id==int(userid)).first()
        user.key=0
        db.session.add(user)
        db.session.commit()
    return jsonify(code=0,message='ok')

#用户列表
@blue.route('/user-list/',methods=['GET','POST'])
def user_list():
    users = User.query.filter_by(key=True)
    page = int(request.args.get('page') or 1)
    paginate = users.paginate(page, 4, False)
    if request.method=="GET":
        num=0
        for i in users:
            num+=1
        data={
            'users':users,
            'num':num,
            'paginate':paginate
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
# @blue.route('/findaByPage/')
# def findByPage():
#     page = int(request.args.get('page') or 1)
#     uspage = User.query.paginate(page,4,False)

# 逻辑恢复用户
@blue.route('/recoverUser/',methods=['POST'])
def recoverUser():
    user_id = json.loads(request.form.get('data'))
    print(user_id)
    for userid in user_id['id']:
        user = User.query.filter(User.id==int(userid)).first()
        user.key=1
        db.session.add(user)
        db.session.commit()
    return jsonify(code=0,message='ok')

#已删除用户
@blue.route('/user-del/',methods=['GET',"POST"])
def user_del():
    if request.method=='POST':
        start = request.form.get('start')
        end = request.form.get('end')
        print(start,end)

    users = User.query.filter_by(key=False)
    page = int(request.args.get('page') or 1)
    paginate = users.paginate(page, 4, False)
    if request.method=="GET":
        num=0
        for i in users:
            num+=1
        data={
            'users':users,
            'num':num,
            'paginate': paginate
        }
        return render_template('./user-del.html',data=data)


# 数据库内删除用户
@blue.route('/foreverDel/',methods=['POST'])
def foreverDel():
    user_id = json.loads(request.form.get('data'))['id']
    user = User.query.filter(User.id==int(user_id)).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify(code=0,message='ok')



#邮件模版
@blue.route('/email-model/',methods=['GET',])
def email_model():
    # return render_template('./email_model.html')
    models = Models.query.filter_by(key=True)
    num = 0
    for i in models:
        num += 1
    data = {
        'models': models,
        'num': num
    }

    return render_template('./email_model.html', data=data)

# 添加模版
@blue.route('/model-add/',methods=["GET",'POST'])
def model_add():
    if request.method=="GET":
        return render_template('./model-add.html')
    if request.method=="POST":
        model_name=request.form.get('model_name')
        model_title=request.form.get('model_title')
        model_msg=request.form.get('model_msg')


        model=Models()
        model.model_name=model_name
        model.title=model_title
        model.msg=model_msg

        t=time.localtime()
        last_data="{}-{}-{}".format(t.tm_year,t.tm_mon,t.tm_mday)
        last_time="{}:{}:{}".format(t.tm_hour,t.tm_min,t.tm_sec)

        model.last_date=last_data
        model.last_time=last_time
        model.key=1
        model.count=0

        sql_model=Models.query.filter_by(model_name=model_name)
        for i in sql_model:
            if i.model_name==model_name:
                return render_template('./yicunzai.html')



        db.session.add(model)
        db.session.commit()

        print(model_name,model_title,model_msg,last_time,last_data)

        return render_template('./successful.html')



# 删除模版
@blue.route('/model-del/',methods=['GET',"POST"])
def model_del():
    # print('ssssssssss'*10)
    if request.method=="GET":
        return render_template('./model-del.html')
    if request.method=="POST":
        model_name=request.form.get('model_name')
        model = Models.query.filter_by(model_name=model_name).first()
        if not model:
            return render_template('./bucunzai.html')
        db.session.delete(model)
        db.session.commit()
        return render_template('./successful.html')






#封装邮箱发送
def sendmail(recv, title, content):
    username='kog365986211@163.com'
    passwd='wangliguo1994'
    msg = MIMEText(content)
    msg['Subject'] = title
    msg['From'] = username
    msg['To'] = recv
    mail_host = 'smtp.163.com'
    port = 25
    smtp = smtplib.SMTP(mail_host, port=port)
    smtp.login(username, passwd)
    smtp.sendmail(username, recv, msg.as_string())
    smtp.quit()
    print('Email Send Success.')

#发送邮箱
@blue.route('/email-model/youjian',methods=['POST',"GET"])
def fasong():
    if request.method=="POST":
        title=request.form.get('title')
        content=request.form.get('desc')
        user=User.query.filter_by(key=True)
        model_name=request.form.get('model_name')

        id_model=Models.query.filter(Models.model_name==model_name).first()
        num = id_model.count

        # 此处每次执行计数
        num2=int(num)+1
        id_model.count=num2
        # 此处每次最后的执行日期和时间
        t = time.localtime()
        last_data = "{}-{}-{}".format(t.tm_year, t.tm_mon, t.tm_mday)
        last_time = "{}:{}:{}".format(t.tm_hour, t.tm_min, t.tm_sec)
        id_model.last_data=last_data
        id_model.last_time=last_time

        db.session.add(id_model)
        db.session.commit()

        t = request.form.get('time')
        if not len(t):

        # 测试已经关闭

            # for i in user:
            #     email=i.email
            #     sendmail(email,title,content)
            # return '发送成功。。。。。'

            pass

        sec = int(t)*60









    if request.method=='GET':
        return render_template('./welcome.html')


#给编辑页面添加ID值
lt = []
@blue.route('/getId/',methods=['POST'])
def putId():
    user_id = json.loads(request.form.get('data'))['id']
    print(user_id)
    if lt:
        lt.clear()
    lt.append(user_id)
    return jsonify(code=0,message='ok')




#修改编辑用户
@blue.route('/user-list/user-edit.html',methods=['GET',"POST"])
def user_edit():
    if request.method=='GET':
        return render_template('./user-edit.html')
    if request.method=="POST":
        print(lt)
        id = lt[0]
        user = User.query.filter(User.id==id).first()
        username=request.form.get('username')
        email=request.form.get('email')
        address=request.form.get('address')

        # 判断数据库是否存在
        sql_user = User.query.filter_by(username=username)
        for i in sql_user:
            if i.username == username:
                return render_template('./2222.html')

        if username:
            if address:
                user.username = username
                user.email = email
                user.address = address
                db.session.add(user)
                db.session.commit()
                return render_template('./successful.html')
            user.username = username
            user.email = email
            db.session.add(user)
            db.session.commit()
            return render_template('./successful.html')
        if address:
            user.email = email
            user.address = address
            db.session.add(user)
            db.session.commit()
            return render_template('./successful.html')
        if email:
            user.email = email
            db.session.add(user)
            db.session.commit()
            return render_template('./successful.html')


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
                return render_template('./2222.html')
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
        return render_template('./successful.html')

#查询到的用户
@blue.route('/select-user/',methods=['GET',])
def select_user():
    user=request.form.get()
    if request.method=='GET':
        return render_template('./select-user.html',user=user)










#测试接口
@blue.route('/test/')
def test11():
    if request.method=='GET':
        names=User.query.all()
        hehe=names[0].key
        print(hehe)

        return render_template('./1111111.html',names=names)
    if request.method=="POST":
        id = request.args.get('id')

        print(id)
        return 'hehda'





















