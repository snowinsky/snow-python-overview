import re
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render

from django.urls import reverse
from django.views import View

from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponse

from django.conf import settings


##########################
# 登录页面操作
##########################
class LoginView(View):
    def get(self, request):
        return render(request, "login/login.html")

    def post(self, request):
        # 1.接收参数
        mobile = request.POST.get("mobile")
        password = request.POST.get("password")
        remember = request.POST.get("remember")
        # 2.参数的验证
        #     2.1 验证手机号
        # if not re.match(r"^[a-zA-Z0-9]{8,20}$", mobile):
        #     return HttpResponseBadRequest("手机号不符合规则")
        #     2.2 验证密码是否符合规则
        # if not re.match(r"^[a-zA-Z0-9]{8,20}$", password):
        #     return HttpResponseBadRequest("密码不符合规则")
        # 3.用户认证登录
        # 采用系统自带的认证方法进行认证
        # 如果我们的用户名和密码正确，会返回user
        # 如果我们的用户名或密码不正确,会返回None
        # 默认的认证的方法 针对于username字段进行用户名的判断
        # 当前的判断信息是  手机号,索引我们需要修改一下认证字段
        user = authenticate(mobile=mobile, password=password)
        # 4.状态的保持
        login(request, user)
        # 5.根据用户选择的是否记住登录状态来进行判断

        # 根据next参数来进行页面的跳转
        next_page = request.GET.get("next")
        if next_page:
            response = redirect(next_page)
        else:
            response = redirect(reverse("category:dashboard"))

        if remember != "on":  # 没有记住用户信息
            # 浏览器关闭后
            request.session.set_expiry(0)
            # 6.为了首页显示我们需要设置一些cookie信息
            response.set_cookie("is_login", True)
            response.set_cookie("username", user.username, max_age=14 * 24 * 3600)
        else:  # 记住用户信息  过期时间2周
            request.session.set_expiry(None)
            response.set_cookie("is_login", True, max_age=14 * 24 * 3600)
            response.set_cookie("username", user.username, max_age=14 * 24 * 3600)
        # 7. 返回相应
        return response


##########################
# 验证码获取
##########################
from login.libs.captcha.simple_captcha import Captcha
class CaptchaView(View):
    def get(self, request):
        # 1.接收前端传递过来的uuid
        captchaId = request.GET.get('captchaId')
        # 2.判断uuid是否获取到
        # if uuid is None:
        #     return HttpResponseBadRequest('没有传递UUID')
        # 3.通过调用captcha来乘车图片验证码
        text, image = Captcha.instance().getPicture()
        # 4.将图片内容保存到redis中
        if captchaId is not None:
            redis_connection = get_redis_connection('default')
        #         uuid作为一个key，图片内容作为一个value，同时我们还需要设置一个时效
        # key设置为uuid
        # seconds 过期秒数  300秒  5 分钟过期时间
        # value  text
            redis_connection.setex("img:%s" % captchaId, 3000, text)
            
            print("set captcha into the redis", captchaId, text)
        # 5. 返回图片二进制
        return HttpResponse(image, content_type="image/jpeg")
    


    
##########################
# 验证码获取
##########################
from django_redis import get_redis_connection

class RedisView(View):
    def get(self, request):
        key = request.GET.get('key')
        if key is None:
            return HttpResponseBadRequest('请使用?key=[value]的格式传递参数')
        redis_client = get_redis_connection("default")
        value = redis_client.get(key)
        return HttpResponse(str(value))
    
    def post(self, request):
        key = request.GET.get('key')
        value = request.GET.get('value')
        if key is None or value is None:
            return HttpResponseBadRequest('请使用?key=[value]&value=[value]的格式传递参数')
        redis_client = get_redis_connection("default")
        ret = redis_client.setex(key, 50, value)
        return HttpResponse(str(ret))
    
    def put(self, request):
        self.post(request)
    
    def delete(self, request):
        key = request.GET.get('key')
        if key is None:
            return HttpResponseBadRequest('请使用?key=[value]的格式传递参数')
        redis_client = get_redis_connection("default")
        value = redis_client.delete(key)
        return HttpResponse(str(value))
    

##########################
# 登出按钮操作
##########################
class LogoutView(View):
    def get(self, request):
        # 1. session数据清除
        logout(request)
        # 2. 删除部分cookie数据
        response = redirect(reverse("home:index"))
        response.delete_cookie("is_login")
        # 3.跳转到首页
        return response


##########################
# 注册页面操作
##########################
import time
from login.models import Login
from django.db import DatabaseError
class RegisterView(View):
    def get(self, request):
        captchaId = str(time.time())
        captchaUrl = settings.BASE_URL + "/login/captcha/?captchaId=" + captchaId
        data = {
            "captchaUrl" : captchaUrl,
            "captchaId" : captchaId,
        }
        return render(request, "login/register.html", data)

    def post(self, request):
        # 1.接收数据
        mobile = request.POST.get("mobile")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        imgage_code = request.POST.get("imgage_code").upper()
        uuid = request.POST.get("uuid")
        print("注册时的验证码使用的uuid是", uuid)
        # 2.验证数据
        #     2.1 参数是否安全
        if not all([mobile, password, password2]):
            return HttpResponseBadRequest("缺少必要的参数！")
        #     2.2 手机号的格式是否正确
        if not re.match(r"^1[3-9]\d{9}$", mobile):
            return HttpResponseBadRequest("手机号不符合规则！")
        #     2.3 密码是否符合格式
        if not re.match(r"^[0-9A-Za-z]{8,20}$", password):
            return HttpResponseBadRequest("请输入8-20为密码，密码是数字，字母！")
        #     2.4 密码和确认密码是否一致
        if password != password2:
            return HttpResponseBadRequest("两次输入密码不一致！")
        #     2.5 验证码是否要一致
        redis_conn = get_redis_connection("default")
        img_code_server = redis_conn.get("img:%s" % uuid)
        print("用uuid从redis获取的验证码是", uuid, img_code_server, img_code_server.decode(), imgage_code)
        if img_code_server is None:
            return HttpResponseBadRequest("图片验证码已过期")
        if imgage_code != img_code_server.decode().upper():
            return HttpResponseBadRequest("图片验证码错误")
        # 3.保存注册信息
        # create_user 可以使用系统的方法来对密码进行加密
        try:
            user = Login.objects.create_user(
                username=mobile, mobile=mobile, password=password
            )
        except DatabaseError as e:
            #logger.error(e)
            return HttpResponseBadRequest("注册失败")
        # 4.返回相应跳转到指定页面
        # redirect 进行重定向
        # reverse 可以通过 namespace:namespace 来获取到视图所对应的路由
        response = redirect(reverse("login:logon"))

        # login() 登录状态保持
        login(request, user)

        # 设置cookie信息，方便 首页中 用户信息的展示和判断
        response.set_cookie("is_login", True)
        response.set_cookie("username", user.username, max_age=7 * 24 * 3600)
        return response
