import typing as t
from flask import request
from functools import wraps
from apps.models.Worker import Worker
def success_api(message: str = "成功", code: int = 200) -> t.Dict:
    """ 成功响应 默认值”成功“ """
    return {'success': True, 'message': message, 'code': code}


def fail_api(message: str = "失败", code: int = 404) -> t.Dict:
    """ 失败响应 默认值“失败” """
    return {'success': False, 'message': message, 'code': code}


def table_api(success: bool = True,
              message: str = "",
              result: t.Union[dict, list] = None,
              code: int = 0) -> t.Dict:

    return {
        'success': success,
        'message': message,
        'code': code,
        'result': result,
    }


def decoratr_white(func):
    @wraps(func)
    def call(*args,**kwargs):
        print('我看看我是不是白名单~~~')
        ip = request.remote_addr
        temp = Worker.query.filter(Worker.ip == ip).first()
        if str(temp)==str(ip):
            print('在白名单内')
            func(*args,**kwargs)
            return func(*args,**kwargs)
        else:
            return fail_api('不在白名单内')
    return call
