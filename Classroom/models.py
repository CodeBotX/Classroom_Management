from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


# ---------- Class Subject khởi tạo đối tượng môn học ----------
class Subject (models.Model):
  name = models.CharField(max_length=50)
  def __str__(self):
    return self.name

# ---------- Class Person là cha của teacher và student ----------
class Person:
  def __init__(self, name):
    self.name = models.CharField(max_length=50)
  
# ----------------------------------------------------------------
# ---------- Class teacher ----------
class Teacher (Person):
  def __init__(self, name,subject):
    super().__init__(name)
    self.subject = models.CharField(max_length=20)
  def grade_student (self,student ,score):
    # cho điểm học sinh
    pass
    
class Student(Person):
  comment = models.TextField()
  def __init__(self, name,id):
    super().__init__(name)
    self.id = models.ImageField(primary_key=True)
  def save(self, *args, **kwargs):
    if not 1000<= self.id <10000:
      raise
    ValidationError("ID Là 4 Số")
    super().save(*args, **kwargs)
    
class Schedule(models.Model):
    DAYS_OF_WEEK = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    ]

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=3, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()
