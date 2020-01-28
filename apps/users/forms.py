# -*- coding: utf-8 -*-
"""
@File        :  forms.py
@Modify Time :  2020/1/25 16:11      
@Author      :  Calvin.zhu    
@Version     :  1.0
@Description :  form用于对post入参等信息的辅助验证
"""
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    """
    继承自forms.Form，实际是有个入参的（dict）
    调用示例：
    LoginForm(request.POST)

    类中定义的变量，必须与html页面中元素的name相同，否则不会被验证
    """
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    """
    继承自forms.Form，实际是有个入参的（dict）
    调用示例：

    类中定义的变量，必须与html页面中元素的name相同，否则不会被验证
    CaptchaField：验证码相关的验证，通过第三方（captcha）扩展
    """
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})     # 定制化的错误提示


class ForgetForm(forms.Form):
    """
    发起密码重置的页面校验
    """
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})     # 定制化的错误提示


class ModifyPwdForm(forms.Form):
    """
    修改密码的校验

    继承自forms.Form，实际是有个入参的（dict）
    类中定义的变量，必须与html页面中元素的name相同，否则不会被验证
    """
    password = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)
