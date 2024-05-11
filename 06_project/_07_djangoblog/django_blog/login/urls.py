from django.urls import path
from login.views import LoginView, CaptchaView, RedisView, RegisterView

app_name = "login"

urlpatterns = [

    path("logon/",    LoginView.as_view(),    name="logon"),
    path("captcha/",  CaptchaView.as_view(),  name="captcha"),
    path("redis/",    RedisView.as_view(),    name="redis"),
    path("register/", RegisterView.as_view(), name="register"),
    
]
