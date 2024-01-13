from django.contrib import admin

# Register your models here.
from .models import Subject,Teacher,Class,Student,Score,Lessons,LessonReview


class Student_Admin (admin.ModelAdmin):
    list_display=['student_ID','student_name','classroom']
    search_fields=['student_ID']
    list_filter =['classroom']

class Class_Admin (admin.ModelAdmin):
    list_display=['class_CODE','teacher']
    search_fields=['class_CODE']
    filter_horizontal = ('subjects',)


class Subject_Admin (admin.ModelAdmin):
    list_display=['subject_CODE','subject_name']
    search_fields=['subject_CODE']



class Teacher_Admin (admin.ModelAdmin):
    list_display=['teacher_ID','get_teacher_name','get_subjects_display']
    search_fields=['teacher_ID']
    filter_horizontal = ('subjects',)
    def get_subjects_display(self, obj):
        return ", ".join([subject.subject_name for subject in obj.subjects.all()])
    get_subjects_display.short_description = 'Subjects'
    
    def get_teacher_name(self, obj):
        return obj.get_teacher_name()
    get_teacher_name.short_description = 'Name'

    
    
class Score_Admin (admin.ModelAdmin):
    list_display=['get_subjects_CODE','get_student_name','get_subjects_CODE','get_subjects_name','K1_score','K2_score','K3_score']
    list_filter = ['student__classroom']
    search_fields=['student__classroom']
    def get_subjects_CODE(self, obj):
        return obj.subject.subject_CODE
    get_subjects_CODE.short_description = 'Subject CODE'
    
    def get_subjects_name(self, obj):
        return obj.subject.subject_name
    get_subjects_name.short_description = 'Subject name'
    
    def get_student_name(self, obj):
        return obj.student.student_name
    get_student_name.short_description = 'Student Name'

    def get_student_ID(self, obj):
        return obj.student.student_ID
    get_student_ID.short_description = 'Student ID'
    



class Lessons_Admin (admin.ModelAdmin):
    list_display=['get_subject_name','get_subjects_CODE','counter','get_teacher_name','get_teacher_ID','schedule_time']
    search_fields=['subject__subject_name','subject__subject_CODE']
    list_filter = ['classroom']
    def get_subject_name(self, obj):
        return obj.subject.subject_name
    get_subject_name.short_description = 'Subject name'
    
    def get_teacher_name(self, obj):
        return obj.teacher.get_teacher_name()
    get_teacher_name.short_description = 'Teacher'
    
    def get_subjects_CODE(self, obj):
        return obj.subject.subject_CODE
    get_subjects_CODE.short_description = 'Subject CODE'
    
    def get_teacher_ID(self, obj):
        return obj.teacher.get_teacher_ID()
    get_teacher_ID.short_description = 'Teacher ID'
    

class LessonReview_Admin (admin.ModelAdmin):
    list_display=['get_lesson','get_teacher_name','get_teacher_ID','get_schedule_time','review','rating']
    search_fields=['lesson']
    list_filter = ['lesson__classroom','lesson__schedule_time']
    def get_lesson(self, obj):
        return f"{obj.lesson.subject.subject_name } - {obj.lesson.counter}"
    get_lesson.short_description = 'Lesson'
    
    def get_teacher_name(self, obj):
        return obj.lesson.teacher.get_teacher_name()
    get_teacher_name.short_description = 'Teacher Name'
    
    def get_teacher_ID(self, obj):
        return obj.lesson.teacher.get_teacher_ID()
    get_teacher_ID.short_description = 'Teacher ID'
    
    def get_schedule_time(self, obj):
        return obj.lesson.schedule_time
    get_schedule_time.short_description = 'Time'

admin.site.register(Subject,Subject_Admin)
admin.site.register(Teacher,Teacher_Admin)
admin.site.register(Class,Class_Admin)
admin.site.register(Student,Student_Admin)

admin.site.register(Score,Score_Admin)
admin.site.register(Lessons,Lessons_Admin)
admin.site.register(LessonReview,LessonReview_Admin)