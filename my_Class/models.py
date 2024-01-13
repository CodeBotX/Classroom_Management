from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class Subject (models.Model):
    subject_CODE = models.CharField(primary_key=True, max_length = 10,unique=True)
    subject_name = models.CharField(max_length = 100)
    def __str__(self):
        return f"{self.subject_CODE}-{self.subject_name}"
    

    
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_ID = models.IntegerField(unique=True)
    subjects = models.ManyToManyField(Subject)
    def get_teacher_ID( self):
        return f"{self.teacher_ID}"
    def get_teacher_name( self):
        return f"{self.user.get_full_name()}"
    def __str__(self)->str:
        return f"{self.user.get_full_name()} - {self.teacher_ID}"

# ---------- Class Lớp học ----------    
class Class(models.Model):
    class_CODE = models.CharField(primary_key=True, max_length = 5)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE, blank=True, null=True)
    subjects = models.ManyToManyField(Subject)
    def __str__(self):
        return  f"{self.class_CODE}"
# ---------- Class student ----------
class Student(models.Model):
    student_ID = models.IntegerField(primary_key=True,auto_created=True)
    student_name = models.CharField(max_length=100)
    classroom = models.ForeignKey(Class, on_delete=models.CASCADE,blank=True, null=True)
    def __str__(self):
        return f"{self.student_name} - {self.student_ID}" 
# ---------- Class Điểm ----------     
class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject= models.ForeignKey(Subject, on_delete=models.CASCADE)
    K1_score = models.FloatField(null=True, blank=True)
    K2_score = models.FloatField(null=True, blank=True)
    K3_score = models.FloatField(null=True, blank=True)
    def clean(self):
        if self.subject not in self.student.classroom.subjects.all():
            raise ValidationError("The selected subject is not one of the subjects that the student is studying.")

    
class Lessons (models.Model):
    classroom = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    schedule_time = models.DateTimeField()
    counter = models.PositiveIntegerField(default=1)  # Thêm trường counter

    def __str__(self):
        return f"{self.classroom} - {self.subject} - {self.teacher} - Tiết {self.counter} - {self.schedule_time}"

    def save(self, *args, **kwargs):
        if not self.pk:  # Nếu đây là một tiết học mới
            last_lesson = Lessons.objects.filter(classroom=self.classroom, subject=self.subject).order_by('-counter').first()
            if last_lesson:
                self.counter = last_lesson.counter + 1
        super().save(*args, **kwargs)
        
class LessonReview(models.Model):
    REVIEW_CHOICES = [
        ('A', 'Giỏi'),
        ('B', 'Tốt'),
        ('C', 'Trung Bình'),
        ('D', 'Kém'),
    ]

    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.CharField(max_length=1, choices=REVIEW_CHOICES)  # Thêm trường xếp loại

    def __str__(self):
        return f"{self.lesson.subject.subject_name} - Review ID: {self.pk} - Rating: {self.rating}"


