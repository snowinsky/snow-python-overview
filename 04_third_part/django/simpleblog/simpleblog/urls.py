"""
URL configuration for simpleblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include

import hello.HelloView as HelloView #引入新增的view

urlpatterns = [
    path("admin/", admin.site.urls),
    ############################## 新增新的view ###################################
    path('hello/str', HelloView.helloStr, name='helloStr'),
    path('hello/html', HelloView.helloHtml, name='helloHtml'),
    
    path("helloapp/", include("helloapp.urls")),
    ############################## 新增新的view ###################################
]
