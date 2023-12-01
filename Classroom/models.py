from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.




# ---------- Class đối tượng các tiết học ----------
class Lesson(models.Model):
    LESSON_GRADE_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]
    lesson_name = models.CharField(max_length=100)
    comment = models.TextField(blank=True)
    grade = models.CharField(max_length=1, choices=LESSON_GRADE_CHOICES)
    schedule_time = models.DateTimeField()

    def __str__(self):
        return f"{self.lesson_name} - {self.schedule_time}"

# ----------------------------------------------------------------


# ---------- Class teacher ----------
class Teacher (models.Model):
  name = models.CharField(max_length=100)
  subject_teacher = models.CharField(max_length=100)
  teacher_id = models.IntegerField(unique=True, validators=[MinValueValidator(100000), MaxValueValidator(999999)])
  def __str__(self):
      return f"{self.name} - {self.teacher_id}"  

# ---------- Class student ----------
class Student(models.Model):
  name = models.CharField(max_length=100)
  student_comment = models.TextField()
  student_id = models.IntegerField(unique=True, validators=[MinValueValidator(100000), MaxValueValidator(999999)])
  grade_Math = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
  grade_english = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
  grade_physics = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
  grade_chemistry = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
  grade_literature = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
  grade_IT = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
  
  def __str__(self):
      return f"{self.name} - {self.student_id}"
