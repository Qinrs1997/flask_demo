from exts import db

import datetime

##创建model模型
class Worker(db.Model):
    #属性

    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    ip= db.Column(db.String(20), nullable = True)
    desc = db.Column(db.String(100))

    def __init__(self,ip,desc):
        self.ip = ip
        self.desc = desc
    def __str__(self):
        return self.ip