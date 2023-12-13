from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.




# ---------- Class teacher ----------
class Teacher (models.Model):
    name = models.CharField(max_length=100)
    subject_teacher = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    def __str__(self):
        return f"{self.name} - {self.teacher_id}"  

    def save(self, *args, **kwargs):
    # Kiểm tra xem id có đúng 6 chữ số hay không
        if len(str(self.id)) != 6:
            raise ValidationError("ID phải có 6 chữ số.")
    
        super().save(*args, **kwargs)

# ---------- Class student ----------
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} - {self.id}"
    def save(self, *args, **kwargs):
        # Kiểm tra xem id có đúng 6 chữ số hay không
        if len(str(self.id)) != 6:
            raise ValidationError("ID phải có 6 chữ số.")
        
        super().save(*args, **kwargs)

class Subjects (models.Model):
    SUBJECT_CHOICES = [
        ('MAT', 'Math'),
        ('ENG', 'English'),
        ('PHY', 'Physics'),
        ('CHE', 'Chemistry'),
        ('LIT', 'Literature'),
        ('CPS', 'computer science'),
    ]
    name = models.CharField(max_length=3, choices=SUBJECT_CHOICES)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.FloatField()
    def __str__(self):
        return f"{self.student.id} - {self.student.name} - {self.name} - {self.score}"
    def save(self, *args, **kwargs):
    # Kiểm tra xem score có đúng 6 chữ số hay không
        if self.score < 0 and self.score>10:
            raise ValidationError("Điểm từ 0 đến 10")
    
        super().save(*args, **kwargs)
        
