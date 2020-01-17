# -*- coding: utf-8 -*-
"""
@File        :  adminx.py
@Modify Time :  2020/1/9 19:44      
@Author      :  Calvin.zhu    
@Version     :  1.0
@Description :  None
"""
import xadmin
from .models import Course, CourseResource, Lesson, Video


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_nums', 'image', 'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_time']
    list_filter = ('add_time',)


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ('course__name', 'add_time', )


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ('add_time',)


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ('add_time', )


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)