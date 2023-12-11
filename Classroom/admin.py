# Dùng để hiển thị các model trong giao diện quản trị Dj. 

from django.contrib import admin
from .models import Teacher
from .models import Student
from .models import Subjects


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subjects)


# Register your models here.

