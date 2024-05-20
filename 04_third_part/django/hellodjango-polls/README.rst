这只是一个简单的例子，将hellodjango工程里边的polls这个app单独拎出来做成一个package，便于别的服务复用。

使用的是setuptools工具

参考的是https://docs.djangoproject.com/zh-hans/5.0/intro/reusable-apps/

使用 python setup.py sdist命令生成一个dist文件夹，里边有个jar包

python -m pip install --user hellodjango-polls/dist/django_polls-0.1.tar.gz