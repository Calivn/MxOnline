# -*- coding: utf-8 -*-
"""
@File        :  email_send.py
@Modify Time :  2020/1/27 13:35      
@Author      :  Calvin.zhu    
@Version     :  1.0
@Description :  None
"""
import random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from MxOnline.settings import EMAIL_FROM


def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type='register'):
    """
    完成验证邮件的发送，并提供注册验证的URL。
    生成验证码，并存储在models.EmailVerifyRecord表中；
    通过Django的mail.send_mail发送注册确认邮件（注意：邮件发送相关参数需要配置在settings中）。

    :param email: 邮件接收人
    :param send_type: models.EmailVerifyRecord中界定的类型
    :return:
    """
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type

    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "注册激活链接"
        email_body = "请点击下面的链接激活账号：http://127.0.0.1:8000/active/{0}".format(code)
    elif send_type == "forget":
        email_title = "重置密码链接"
        email_body = "请点击下面的链接重置账号密码：http://127.0.0.1:8000/reset/{0}".format(code)

    send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])

    if send_status:
        email_record.save()     # 如果邮件发送成功,则将生成注册的随机验证码，并存入EmailVerifyRecord表中

    return send_status
