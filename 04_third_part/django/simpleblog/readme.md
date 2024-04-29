# simpleblog

## django-admin startproject simpleblog
> 使用脚手架创建工程模板
>
~~~
PS D:\ws-py\snow-python-overview\04_third_part\django> django-admin startproject simpleblog
PS D:\ws-py\snow-python-overview\04_third_part\django> cd simpleblog
PS D:\ws-py\snow-python-overview\04_third_part\django\simpleblog> python .\manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.    
Run 'python manage.py migrate' to apply them.
April 28, 2024 - 11:05:35
Django version 4.2.11, using settings 'simpleblog.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
~~~

http://127.0.0.1:8000/admin 可以打开则表示脚手架创建工程成功

## 更改数据库为MySQL，不用sqlite3

修改settings.py文件

~~~
DATABASES = {
    "default": {
        # "ENGINE": "django.db.backends.sqlite3",
        # "NAME": BASE_DIR / "db.sqlite3",
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '123456',
        'NAME': 'simpleblog',
    }
}
~~~

~~~
PS D:\ws-py\snow-python-overview\04_third_part\django\simpleblog> python .\manage.py migrate  
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
PS D:\ws-py\snow-python-overview\04_third_part\django\simpleblog> 
~~~

一堆表被自动创建

## 创建超级用户

~~~
PS D:\ws-py\snow-python-overview\04_third_part\django\simpleblog> python .\manage.py createsuperuser
Username (leave blank to use 'jack.ji'): jack.ji
Email address: jack.ji@snow.com
Password: 
Password (again):
Error: Your passwords didn't match.
Password: 
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
PS D:\ws-py\snow-python-overview\04_third_part\django\simpleblog> 
~~~

在刚才的admin网页上输入用户名密码就可以登录进去了


## 创建一个新的功能模块，也就是project下创建一个新的app

- python manage.py startapp [newAppName]
- modeles.py中加入业务entity的定义，就是数据库表的各个字段的定义信息
- views.py中加入对外开放的method的定义
- urls.py中加入views中各个method的url
- 在主urls中把这个app的urls加载进去
- 在settings.py中把这个新的app的apps.py中的Conf注册进去
- python manage.py makemigrations [newAppName]激活这个新的app
- python manage.py migrate 将[newAppName]中新定义的表新建到数据库里

> $ python manage.py sqlmigrate polls 0001 可以用这个命令看看有哪些sql会被执行

~~~
PS D:\ws-py\snow-python-overview\04_third_part\django\simpleblog> python .\manage.py makemigrations helloapp
Migrations for 'helloapp':
  helloapp\migrations\0001_initial.py
    - Create model Question
    - Create model Choice
PS D:\ws-py\snow-python-overview\04_third_part\django\simpleblog> python .\manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, helloapp, sessions
Running migrations:
  Applying helloapp.0001_initial... OK
~~~

## 创建虚拟环境

~~~
python3 -m venv tutorial_env
source tutorial_env/bin/activate
这将在tutorial_env子目录中创建新的虚拟环境，并配置当前shell以将其用作默认python环境。
~~~

