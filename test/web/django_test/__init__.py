# Python下有许多款不同的 Web 框架。Django是重量级选手中最有代表性的一位。许多成功的网站和APP都基于Django。
# Django采用了MVC的软件设计模式，即模型M，视图V和控制器C。
# 安装
# $ pip install django
#
# 配置环境变量: D:\Python36\Lib\site-packages\django\bin;
# 添加完成后就可以使用Django的django-admin.py命令新建工程了。
#
# 检查是否安装成功
# $ import django
# $ django.get_version()
#
# 测试版本说明：
# Python 3.6
# Django 2.0.3
#
# Django 管理工具
# 使用 django-admin.py 来创建 HelloWorld 项目：
# $ django-admin.py startproject HelloWorld
#
# 创建完成后我们可以查看下项目的目录结构：
# $ cd HelloWorld/
# $ tree
# .
# |-- HelloWorld
# |   |-- __init__.py
# |   |-- settings.py
# |   |-- urls.py
# |   `-- wsgi.py
# `-- manage.py
#
# 目录说明：
#     HelloWorld: 项目的容器。
#     manage.py: 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互。
#     HelloWorld/__init__.py: 一个空文件，告诉 Python 该目录是一个 Python 包。
#     HelloWorld/settings.py: 该 Django 项目的设置/配置。
#     HelloWorld/urls.py: 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"。
#     HelloWorld/wsgi.py: 一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。
#
# 接下来我们进入 HelloWorld 目录输入以下命令，启动服务器：
# $ python manage.py runserver 0.0.0.0:8000
#
# 0.0.0.0 让其它电脑可连接到开发服务器，8000 为端口号。如果不说明，那么端口号默认为 8000。
#
#
# Django 模型
# Django 对各种数据库提供了很好的支持，包括：PostgreSQL、MySQL、SQLite、Oracle。
# Django 为这些数据库提供了统一的调用API。 我们可以根据自己业务需求选择不同的数据库。
#
# 安装 mysql 驱动
# $ pip install mysqlclient
#
# 修改项目的 settings.py 文件中找到 DATABASES 配置项
#
# 定义模型
# Django规定，如果要使用模型，必须要创建一个app。我们使用以下命令创建一个 TestModel 的 app
# $ django-admin.py startapp TestModel
#
# 接下来在settings.py中找到INSTALLED_APPS这一项
# 'TestModel',               # 添加此项
#
# 在命令行中运行：
# $ python manage.py migrate   # 创建表结构
# $ python manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
# $ python manage.py migrate TestModel   # 创建表结构
#
# 看到几行 "Creating table…" 的字样，你的数据表就创建好了。
# 表名组成结构为：应用名_类名（如：TestModel_test）。
# 注意：尽管我们没有在models给表设置主键，但是Django会自动添加一个id作为主键。
