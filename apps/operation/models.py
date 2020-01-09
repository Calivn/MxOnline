# _*_ encoding:utf-8_*_
from datetime import datetime

from django.db import models

from users.models import UserProfile
from courses.models import Course


# Create your models here.
class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name="姓名")
    mobile = models.CharField(max_length=11, verbose_name="手机")
    course_name = models.CharField(max_length=100, verbose_name="课程名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name


# models的继承
# class UserCourse(models.Model):
#     user = models.ForeignKey(UserProfile, verbose_name="用户名", on_delete=models.PROTECT)
#     course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.PROTECT)
#     add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
#
#     class Mate:
#         verbose_name = "用户课程"
#         verbose_name_plural = verbose_name
#
#
# class CourseComments(UserCourse):
#     """课程评论"""
#     # on_delete=models.PROTECT 阻止上面的删除操作，弹出ProtectedError异常
#     user = models.ForeignKey(UserProfile, verbose_name="用户名", on_delete=models.PROTECT)
#     course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.PROTECT)
#     comments = models.CharField(max_length=200, verbose_name="评论")
#     add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
#
#     class Mate(UserCourse.Mate):
#         verbose_name = "课程评论"
#         verbose_name_plural = verbose_name
class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="用户名", on_delete=models.PROTECT)
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.PROTECT)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户课程"
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    """课程评论"""
    # on_delete=models.PROTECT 阻止上面的删除操作，弹出ProtectedError异常
    user = models.ForeignKey(UserProfile, verbose_name="用户名", on_delete=models.PROTECT)
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.PROTECT)
    comments = models.CharField(max_length=200, verbose_name="评论")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    # on_delete=models.PROTECT 阻止上面的删除操作，弹出ProtectedError异常
    user = models.ForeignKey(UserProfile, verbose_name="用户名", on_delete=models.PROTECT)
    # course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.PROTECT)
    fav_id = models.IntegerField(default=0, verbose_name="数模id")
    fav_type = models.IntegerField(choices=((1, "课程"), (2, "课程机构"), (3, "讲师")), default=1, verbose_name="收藏类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name="接受用户id")  # 如果为0，则将消息发全员
    message = models.CharField(max_length=500, verbose_name="消息内容")
    has_read = models.BooleanField(max_length=False, verbose_name="是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name



