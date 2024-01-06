from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.views.generic import TemplateView


# from django.http import HttpResponseRedirect

# Create your views here.


# view lớp học
@login_required(login_url='/login/')
def classroom_view(request):
    mystudents = Student.objects.all()
    template = loader.get_template('classroom.html')
    context = {
        'myStudents' : mystudents,
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


class siteLoginView ( TemplateView ):
  #  tạm thời để login 2
  template_name = 'login.html' 