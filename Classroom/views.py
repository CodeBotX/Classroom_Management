from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# from django.http import HttpResponseRedirect

# Create your views here.


def classroom(request):

    template = loader.get_template('classroom.html')
    # context = {
    #     'myStudents' : mystudents,
    # }
    return HttpResponse(template.render())