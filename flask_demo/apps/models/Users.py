from exts import db

import datetime

##创建model模型
class User(db.Model):
    #属性

    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    username = db.Column(db.String(15), nullable = False)
    passward = db.Column(db.String(50), nullable = False)
    phone= db.Column(db.String(11), nullable = True)
    restime = db.Column(db.DateTime, nullable = True,default = datetime.datetime.now())
    email = db.Column(db.String(50), nullable = False)
    def __init__(self,username,passward,phone,email):
        self.username = username
        self.passward = passward
        self.phone = phone
        self.email = email
    def __str__(self):
        return self.username