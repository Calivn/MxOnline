# -*- coding: utf-8 -*-
"""
@File        :  adminx.py
@Modify Time :  2020/1/10 16:38      
@Author      :  Calvin.zhu    
@Version     :  1.0
@Description :  None
"""
import xadmin
from .models import City, CourseOrg, Teacher


class CityAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ('add_time',)


class CourseOrgAdmin(object):
    list_display = ['city', 'name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ('city', 'add_time',)


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position',
                    'points', 'click_nums', 'fav_nums', 'image', 'add_time']
    search_fields = ['name', 'work_company', 'work_position', 'points']
    list_filter = ('org__name', 'work_years',)


xadmin.site.register(City, CityAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
