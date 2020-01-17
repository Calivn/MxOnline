# -*- coding: utf-8 -*-
"""
@File        :  adminx.py
@Modify Time :  2020/1/9 18:49      
@Author      :  Calvin.zhu    
@Version     :  1.0
@Description :  adminx文件中的类，都需要xadmin.site.register后，才有效
"""
import xadmin
from .models import EmailVerifyRecord, Banner
from xadmin import views


class BaseSetting(object):
    enable_themes = True    # 启用主题
    use_bootswatch = True   # 增加更多基础主题


class GlobalSettings(object):
    site_title = "朱诚的测试后台"  # 页头
    site_footer = "Calvin.zhu"  # 页脚
    menu_style = "accordion"  # app列表收缩


class EmailVerifyRecordAdmin(object):
    list_display = ['id', 'code', 'email', 'send_type', 'send_time']
    search_fields = ['id', 'code', 'email']
    list_filter = ('send_type', 'send_time',)


class BannerAdmin(object):
    list_display = ['id', 'title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ('send_time',)


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
