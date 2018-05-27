# 视图

from django.http import HttpResponse
from django.shortcuts import render


# 输出字符串
def first(request):
    return HttpResponse("Hello, World!")

# 使用模板
def hello(request):
    context = {'name': 'Horace'}
    return render(request, 'hello.html', context)

def list(request):
    context = {}
    context['list'] = ['Java', 'C#', 'Python', 'Node.js', 'Ruby', 'PHP', 'JavaScript']
    return render(request, 'list.html', context)

# 其他的例子:
# 模型：http://www.runoob.com/django/django-model.html
# 表单：http://www.runoob.com/django/django-form.html
