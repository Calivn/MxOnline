# _*_ encoding:utf-8_*_
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    重写user表，用自己创建的UserProfile覆盖User表

    # 备注用verbose_name，而不是validators
    # A validator is a callable that takes a value and raises a ValidationError if it doesn’t meet some criteria.
    # Validators can be useful for re-using validation logic between different types of fields.
    """
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="zc")
    birthday = models.DateField(verbose_name=u"生日", null=True)
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")),
                              default="female", verbose_name="性别")
    address = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100)

    class Meta:
        # 给模型类起一个更可读的名字
        # 即 在后台管理中，将该表显示为verbose_name定义的值
        verbose_name = "用户信息"
        # 指定模型的复数形式是什么
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.CharField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(choices=(("register", "注册"), ("forget", "找回密码")),
                                 max_length=10, verbose_name="验证码类型")
    # datetime.now：class实例化时调用
    # datetime.now()：model编译时就会调用
    send_time = models.DateTimeField(default=datetime.now, verbose_name="发送时间")

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name="轮播图", max_length=100)
    url = models.URLField(max_length=200, verbose_name="访问地址")
    index = models.IntegerField(default=100, verbose_name="顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

