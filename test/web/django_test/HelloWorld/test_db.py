from django.http import HttpResponse
from test.web.django_test.HelloWorld.TestModel.models import Student

# 添加数据
def add(request):
    stu = Student(name='张三')
    stu.save()
    return HttpResponse("<p>数据添加成功!</p>")

# 修改数据
def update(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = Student.objects.get(id=1)
    test1.name = '李四'
    test1.save()

    # 另外一种方式
    # Test.objects.filter(id=1).update(name='Google')

    # 修改所有的列
    # Test.objects.all().update(name='Google')

    return HttpResponse("<p>修改成功</p>")


# 删除数据
def delete(request):
    # 删除id=1的数据
    test1 = Student.objects.get(id=1)
    test1.delete()

    # 另外一种方式
    # Test.objects.filter(id=1).delete()

    # 删除所有数据
    # Test.objects.all().delete()

    return HttpResponse("<p>删除成功</p>")

# 查询数据
def select(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Student.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Student.objects.filter(id=1)

    # 获取单个对象
    response3 = Student.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    Student.objects.order_by('name')[0:2]

    # 数据排序
    Student.objects.order_by("id")

    # 上面的方法可以连锁使用
    Student.objects.filter(name="runoob").order_by("id")

    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")