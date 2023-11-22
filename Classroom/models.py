from django.db import models

# Create your models here.

# ---------- Class Member khởi tạo các thành viên quản lý ----------
class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  joined_date = models.DateField(null=True)

  # def __str__(self):
  #   return f"{self.firstname} {self.lastname}"

# -------------------------------------------------------------------

# ---------- Class Subject khởi tạo đối tượng môn học ----------
class Subject (models.Model):
  name = models.CharField(max_length=50)
  def __str__(self):
    return self.name

# ---------- Class Person là cha của teacher và student ----------
class Person:
  def __init__(self, name):
    self.name = name
  
# ----------------------------------------------------------------
# ---------- Class teacher ----------
class Teacher (Person):
  def __init__(self, name,subject):
    super().__init__(name)
    self.subject = subject