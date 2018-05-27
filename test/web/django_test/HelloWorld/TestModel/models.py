from django.db import models

# 学生信息类
class Student(models.Model):
    name = models.CharField(max_length=20)