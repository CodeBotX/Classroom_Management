from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
# from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.views.generic import TemplateView, ListView, DetailView
from datetime import datetime
from .forms import *
from django.contrib.auth.views import LoginView

# from django.http import HttpResponseRedirect

# Create your views here.


classroom = Class.objects.get(class_CODE='6A')
# view lớp học
@login_required(login_url='/home/')
def classroom_view(request):
  now = datetime.now()
  classroom = Class.objects.get(class_CODE='6A')
  students = Student.objects.filter(classroom=classroom)
  template = loader.get_template('classroom.html')
  context = {
      'class':classroom,
      'Students' : students,
      'current_time':now,
  }
  return HttpResponse(template.render(context,request))

#  view đăng kí 
def register_view (request):
  form = RegistrationForm()
  template = loader.get_template('register.html')
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/')
  context = {
    'form': form
  }
  return HttpResponse(template.render(context,request))

def student_detail(request, student_ID):
  student = get_object_or_404(Student, pk=student_ID)
  scores = Score.objects.filter(student=student)
  template = loader.get_template('details.html')
  context = {
    'student': student,
    'scores': scores
  }
  return HttpResponse(template.render(context,request))


  
class CustomLoginView(LoginView):
  authentication_form = CustomLoginForm

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['form_student_ID'] = StudentIDForm()
      return context
  def post(self, request, *args, **kwargs):
      form = StudentIDForm(request.POST)
      if form.is_valid():
          student_id = form.cleaned_data['student_id']

          return redirect('student_grade_view', student_ID=student_id)
      else:
          return super().post(request, *args, **kwargs)

def student_grade_view(request, student_ID):
  student = get_object_or_404(Student, pk=student_ID)
  scores = Score.objects.filter(student=student)
  template = loader.get_template('student_grade.html')
  context = {
    'student': student, 
    'scores': scores
  }
  return HttpResponse(template.render(context,request))

# student_grade/<int:student_ID>
# student_grade/<int:student_ID>

def week_summary_view(request):
  reviews = LessonReview.objects.all()  # Lấy tất cả đánh giá
  template = loader.get_template('week_summary.html')
  context = {
    'week_review':reviews
  }
  return HttpResponse(template.render(context,request))

from django.shortcuts import render, redirect
from .models import Class

# def subject_view(request, class_code):
#     if request.method == 'POST':
#         subject_code = request.POST.get('subject_code')
#         # Xử lý lựa chọn của người dùng ở đây...
#         # Ví dụ: chuyển hướng đến một trang khác với subject_code
#         return redirect('some_view_name', subject_code=subject_code)
#     else:
#         class_obj = Class.objects.get(class_CODE=class_code)
#         subjects = class_obj.subjects.all()
#         return render(request, 'classroom.html', {'subjects': subjects})

# def option_view(request):
#     template = loader.get_template('option.html')
#     classes = Class.objects.all()
#     if request.method == 'POST':
#         class_code = request.POST.get('class_code')
#         class_obj = Class.objects.get(class_CODE=class_code)
#         subjects = class_obj.subjects.all()
#     else:
#         subjects = None

#     context = {
#         'classes': classes,
#         'subjects': subjects
#     }
#     return HttpResponse(template.render(context, request))



def option_view(request):
    if request.method == 'POST':
        class_code = request.POST.get('class_code')
        classroom = Class.objects.get(class_CODE=class_code)
        subjects = classroom.subjects.all()
    else:
        classroom = None
        subjects = None

    classes = Class.objects.all()
    context = {
        'classroom': classroom,
        'subjects': subjects,
        'classes': classes,
    }
    return render(request, 'Option.html', context)
