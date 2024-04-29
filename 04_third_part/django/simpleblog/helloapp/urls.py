from django.urls import path

from . import views

app_name = 'helloapp' #为了区分url，需要添加命名空间，让url函数可以认得出来
urlpatterns = [
    path("", views.index, name="index"),
]