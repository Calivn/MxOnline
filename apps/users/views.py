from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm
from utils.email_send import send_register_email


class CustomBackend(ModelBackend):
    """
    本方法通过重写ModelBackend，对用户登陆验证加入email校验，使得登陆时既可以用username，也可以用Email

    Q 用来设置并集查询条件，| 表示或
    示例：
    Q(username=username) | Q(email=username， username=username)
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            # 通过check_password方法，将明文的password转换为密文，并进行校验
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class RegisterView(View):
    """
    用户注册

    校验注册信息,如满足条件,即发送激活邮件
    如邮件发送成功,则将用户信息保存在UserProfile表,将激活信息保存在EmailVerifyRecord表
    """

    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {"register_form": register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            if UserProfile.objects.filter(email=user_name):
                # 这里返回register_form，用于页面填写信息的回填
                return render(request, "register.html", {"register_form": register_form, "msg": "用户已存在"})
            pass_word = request.POST.get('password', '')
            user_profile = UserProfile()  # models中自定义的UserProfile类,代表一张表啊(users_userprofile)
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)  # 对明文密码进行加密

            if send_register_email(user_name):  # 注册类型默认是register
                user_profile.save()  # 注册邮件发送成功,则将注册信息存入数据库
                return render(request, "login.html")
            else:
                return render(request, "register.html", {"register_form": register_form, "msg": "邮件发送失败!"})
        else:
            return render(request, "register.html", {"register_form": register_form})


class ActiveView(View):
    """
    激活注册用户

    先从EmailVerifyRecord中取出active_code对应的验证码记录
    根据其中的邮箱,获取到UserProfile表中的用户信息
    如以上信息都存在,即更新UserProfile表的is_active为true

    注意:active_code与urls中配置的url变量段相同
    """

    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)  # 查询出所有的满足条件的记录
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()  # 别忘了保存
                record.delete()  # 顺便把验证码删了把,要不然可能会越来越多
            return render(request, "login.html")
        else:
            return render(request, "notice_page.html", {"msg": "fail"})  # 如果激活链接不存在，则跳转到这个错误页面


class ForgetView(View):
    """
    发起忘记密码重置动作

    校验用户邮箱信息，如存在则向邮箱发送重置密码链接
    """

    def get(self, request):
        forget_form = ForgetForm()
        return render(request, "forgetpwd.html", {"forget_form": forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email', '')
            if UserProfile.objects.filter(email=email):
                if send_register_email(email, "forget"):
                    return render(request, "notice_page.html", {"msg": "send_success"})
                else:
                    return render(request, "forgetpwd.html", {"forget_form": forget_form, "msg": "邮件发送失败!"})
            else:
                return render(request, "forgetpwd.html", {"forget_form": forget_form, "msg": "用户不存在"})
        else:
            return render(request, "forgetpwd.html", {"forget_form": forget_form})


class ResetView(View):
    """
    重置用户密码

    当前代码：
    校验邮件中的修改密码链接，引导跳转至密码修改页面，并将用户email传递给前端

    注释部分代码：
    先从EmailVerifyRecord中取出reset_code对应的验证码记录
    根据其中的邮箱,获取到UserProfile表中的用户信息
    如以上信息都存在,即更新UserProfile表的password为admin12345

    注意:active_code与urls中配置的url变量段相同
    """

    def get(self, request, reset_code):
        all_records = EmailVerifyRecord.objects.filter(code=reset_code)
        if all_records:
            for record in all_records:
                email = record.email
                # 通过重置链接直接重置成默认密码
                # user = UserProfile.objects.get(email=email)
                # user.password = make_password("admin12345")     # 将密码默认重置为admin12345
                # user.save()  # 别忘了保存
                # record.delete()  # 顺便把验证码删了把，否则这个链接会一直有效
                # return render(request, "login.html")
                return render(request, "password_reset.html", {"email": email})
        else:
            return render(request, "notice_page.html", {"msg": "fail"})


class ModifyPwdView(View):
    """
    通过页面修改密码

    校验两次密码是否相同，满足条件，即修改用户密码
    """

    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password", "")
            pwd2 = request.POST.get("password2", "")
            email = request.POST.get("email", "")
            if pwd1 == pwd2:
                user = UserProfile.objects.get(email=email)
                user.password = make_password(pwd1)  # 保存密文密码
                user.save()  # 别忘了保存
                EmailVerifyRecord.objects.get(email=email).delete()  # 顺便把验证码删了，否则这个链接会一直有效
                return render(request, "login.html")
            else:
                return render(request, "password_reset.html", {"email": email, "msg": "两次输入密码不同"})
        else:
            email = request.POST.get("email", "")  # 密码规则校验不通过，也需要返回email，否则页面无法带回用户信息
            return render(request, "password_reset.html", {"email": email, "modify_form": modify_form})


# <editor-fold desc="用def的方式实现用户登陆验证（不推荐）">
# def user_login(request):
#     """
#     用户登陆验证，并根据验证结果跳转相应页面
#     :param request:
#     :return:render(request, xxx)
#     """
#     if request.method == 'POST':
#         user_name = request.POST.get('username', '')
#         pass_word = request.POST.get('password', '')
#         user = authenticate(username=user_name, password=pass_word)
#         if user is not None and user.is_active:
#             # 注意不要写成request.user.is_active
#             login(request, user)
#             return render(request, "index.html")
#         elif not user.is_active:
#             return render(request, "login.html", {"msg": "用户未激活"})
#         else:
#             return render(request, "login.html", {"msg": "用户名或密码错误"})
#     elif request.method == 'GET':
#         return render(request, "login.html", {})
# </editor-fold>


class LoginView(View):
    """
    用class的方式实现用户登陆。
    核心在所继承的View类。View类将会帮助判断应该调用get还是post还是其他
    """

    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)  # 这是一个dict
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                # 注意不要写成request.user.is_active，这个值一直False
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html")
                else:
                    return render(request, "login.html", {"msg": "用户未激活"})
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误"})
        else:
            return render(request, "login.html", {"login_form": login_form})
