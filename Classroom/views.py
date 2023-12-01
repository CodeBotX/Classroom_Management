from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import RegistrationForm
from django.http import HttpResponseRedirect

# from django.http import HttpResponseRedirect

# Create your views here.


def classroom(request):

    template = loader.get_template('classroom.html')
    # context = {
    #     'myStudents' : mystudents,
    # }
    return HttpResponse(template.render())


def register (request):
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