"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.views.static import serve
import xadmin

# from users import views   # 用函数方式实现登陆时，需要导入的方法
from users.views import LoginView, RegisterView, ActiveView, ResetView, ForgetView, ModifyPwdView
from organization.views import OrgView
from MxOnline import settings

urlpatterns = [
    url('^xadmin/', xadmin.site.urls, name='xadmin'),
    url('^$', TemplateView.as_view(template_name="index.html"), name="index"),
    # 登陆方法用“函数”实现
    # url('^login/$', views.user_login, name="user_login"),
    # 登陆方法用“类”实现, as_view()来自于LoginView所继承的View类
    url(r'^login/$', LoginView.as_view(), name="user_login"),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^captcha/', include('captcha.urls')),     # 验证码相关的包
    url(r'^active/(?P<active_code>.*)/$', ActiveView.as_view(), name="user_active"),    # 注册激活链接
    url(r'^forgetpwd/$', ForgetView.as_view(), name="forgetpwd"),       # 忘记密码
    url(r'^reset/(?P<reset_code>.*)/$', ResetView.as_view(), name="reset_pwd"),    # 打开修改密码页面
    url(r'^modify/$', ModifyPwdView.as_view(), name="modify_pwd"),      # 修改密码

    url(r'^org_list/$', OrgView.as_view(), name="org_list"),       # 机构列表页面

    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),    # 文件上传后，通过该配置进行访问
]
