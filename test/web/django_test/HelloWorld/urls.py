"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

    注意：项目中如果代码有改动，服务器会自动监测代码的改动并自动重新载入，所以如果你已经启动了服务器则不需手动重启。
"""
from django.conf.urls import url
from . import view
# from . import test_db

urlpatterns = [
    url(r'^$', view.first),
    url(r'^hello$', view.hello),
    url(r'^list$', view.list),
    # url(r'^stu/select$', test_db.select),
    # url(r'^stu/add$', test_db.add),
    # url(r'^stu/update$', test_db.update),
    # url(r'^stu/delete$', test_db.delete),
]
