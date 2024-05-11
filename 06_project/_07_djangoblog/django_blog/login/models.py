from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class Login(AbstractUser):
    # 手机号
    mobile = models.CharField(max_length=11, unique=True, blank=False)

    # 头像信息
    avatar = models.ImageField(upload_to="avatar//%Y%m%d", blank=True)

    # 简介信息
    user_desc = models.CharField(max_length=500, blank=True)

    # 修改认证的字段为mobile
    USERNAME_FIELD = "mobile"

    # 创建超级管理员必须输入的字段(不包括  手机号和密码)
    REQUIRED_FIELDS = ["username", "email"]

    class Meta:
        db_table = "t_login"  # 修改表名
        verbose_name = "登录用户"  # admin 后台显示
        verbose_name_plural = "登录用户们"  # admin后台显示

    def __str__(self):
        return "username={}, mobile={}".format(self.username, self.mobile)
