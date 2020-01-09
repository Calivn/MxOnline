# -*- coding: utf-8 -*-
"""
@File        :  adminx.py
@Modify Time :  2020/1/9 18:49      
@Author      :  Calvin.zhu    
@Version     :  1.0
@Description :  None
"""
import xadmin
from .models import EmailVerifyRecord

xadmin.site.site_header = "Calvin's Project"
xadmin.site.site_title = "Welcome"
xadmin.site.index_title = "管理后台"


class EmailVerifyRecordAdmin(object):
    list_display = ('id', 'code', 'email', 'send_type')


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
