#!/usr/bin/python
# coding:utf-8
import requests
import random

def getrate_random():
    list1 = ''
    for i in range(4):
        yan = random.randint(0,9)
        list1+=str(yan)
    return str(list1)

def Email_captcha(email_addr):
    url = "https://api.sendcloud.net/apiv2/mail/send"
    # 您需要登录SendCloud创建API_USER，使用API_USER和API_KEY才可以进行邮件的发送。
    captcha = getrate_random()
    print(captcha)
    params = {"apiUser": "sc_y5xqyo_test_pVSPft",
              "apiKey": "53cca5c2fc4d4bb656da963c13bc1c82",
              "from": "service@sendcloud.im",
              "fromName": "这是邮件吗",
              "to": email_addr,
              "subject": "快来看看结果是啥吧！",
              "html": captcha,
              }

    r = requests.post(url, files={}, data=params)
    print(r.text)
    return captcha

# print(Email_caput("975076417@qq.com"))
