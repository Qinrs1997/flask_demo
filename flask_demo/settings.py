

class Config:
    DEBUG = False
    TESTING = False
    #sqlalchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/mydb'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_ECHO = False
    # SQLALCHEMY_POOL_RECYCLE = 8

class DevelpoConfig(Config):
    DEBUG = True
    ENV = 'development'



"""
1.注册接口 - http://127.0.0.1:8000/v1/api/register
    传参： username : 
          password:
          phone:
          email:
"""
