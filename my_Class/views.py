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
      'current_time':now
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