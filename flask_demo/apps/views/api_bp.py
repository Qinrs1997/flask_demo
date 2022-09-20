from apps.models.Users import User
from flask import Blueprint,request
from exts import db
from flask_restful import Api, Resource
from flask_restful.reqparse import RequestParser
from exts.utils import success_api,fail_api,table_api,decoratr_white
import hashlib,re

api_bp = Blueprint('api_bp',__name__,url_prefix='/v1/api')
api = Api(api_bp)
# api.representation('application/json')

##注册+修改密码
class Register(Resource):
    def get(self):
        #  最新版本的flask不支持该写法  绞尽脑汁以后做出的结论。~！！ 暂时先用reques模块
        # rp.add_argument('a',type=str,help='不能位空', location=['json','form','args'], required=True)
        # # res = rp.parse_args()
        # args = rp.parse_args(strict=False)

        a = request.args.get('a')
        print(a)
        return success_api()
    def post(self):
        """
        username :
        password:
        phone:
        email:

        """
        ##获取前段数据  接受数据
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        email = request.form.get('email')
        print(username, password, repassword, phone, email)

        if re.match("^(?:(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])).*$", username) == None:
            return fail_api(code=203, message="用户名必须是大小写字母+数字，请检查！")
        if re.match("^(?:(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])).*$", password) == None:
            return fail_api(code= 203, message="密码必须是大小写字母+数字，请检查！")

        ###先看看有没有重复
        alluser = User.query.all()
        for role in alluser:
            if str(username)==str(role):
                return fail_api("已存在账户名")

        if  password==repassword:
            pwd = hashlib.sha1(password.encode('utf-8')).hexdigest()
            #print('jiami',pwd)
            user = User(username,pwd,phone,email)
            db.session.add(user)
            db.session.commit()
            return success_api("注册成功")
        else:
            return fail_api("两次账号密码不一致")
    def put(self):
        #修改密码
        username = request.form.get('username')
        password = request.form.get('password')
        newpassword = request.form.get('newpassword')
        phone = request.form.get('phone')
        email = request.form.get('email')
        print(username, password, newpassword, phone, email)

        alluser = db.session.query(User.username,User.passward,User.email).all()
        ###邮箱找回~
        print(alluser)
        for i in range(len(alluser)):
            if  username==alluser[i][0] and email==alluser[i][2]:
                #假装可以修改密码
                print('假装修改数据',newpassword)
                pwd = hashlib.sha1(password.encode('utf-8')).hexdigest()
                User.query.filter(User.email==email,User.username==username).update({"passward":pwd})
                db.session.commit()
                return success_api('修改密码成功')

        return fail_api("修改密码失败")

##登录
class Loginin(Resource):
    def post(self):
        """
        username :
        password:
        """
        ##获取前段数据  接受数据
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)
        pwd = hashlib.sha1(password.encode('utf-8')).hexdigest()
        #查数据
        temp = User.query.filter(User.username==username).first()
        print(temp.passward)
        if pwd==temp.passward:
            return success_api('登录成功')
        return fail_api('账号或密码错误')


##白明单增删改查

class TestDemo(Resource):
    method_decorators = [decoratr_white]
    def get(self):
        alluser = User.query.all()
        data = [{
            'username':item.username,
            'password':item.passward,
            'phone':item.phone,
            'email':item.email
        } for item in alluser
        ]

        return table_api(result=data,code=200,message='成功')
    def post(self):
        ##获取前段数据  接受数据
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        email = request.form.get('email')
        print(username, password, repassword, phone, email)

        ###先看看有没有重复
        alluser = User.query.all()
        for role in alluser:
            if str(username) == str(role):
                return fail_api("已存在账户名")

        if password == repassword:
            pwd = hashlib.sha1(password.encode('utf-8')).hexdigest()
            # print('jiami',pwd)
            user = User(username, pwd, phone, email)
            db.session.add(user)
            db.session.commit()
            return success_api("注册成功")
        else:
            return fail_api("两次账号密码不一致")
    def put(self):
        # 修改密码
        username = request.form.get('username')
        password = request.form.get('password')
        phone = request.form.get('phone')
        print('修改手机号',username,phone)
        temp = User.query.filter(User.username == username).update({"phone": phone})
        db.session.commit()

        return success_api('修改手机号')
    def delete(self):
        id = request.form.get('id')
        User.query.filter(User.id == id).delete()
        db.session.commit()
        return success_api('删除成功')



api.add_resource(Register,'/register')
api.add_resource(Loginin,'/loginin')
api.add_resource(TestDemo,'/testdemo')

#ip = request.remote_addr