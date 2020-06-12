from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Project

def home(request):
	#return HttpResponse('<p>home view</p>')
	#projects = Project.objects.all()
	return render(request, 'home.html')

def resume(request):
	return render(request, 'resume.html')

def about(request):
	return render(request, 'about.html')

def projects(request):
	projs = Project.objects.all()
	return render(request, 'projects.html', {'projs' : projs})

def contact(request):
	return render(request, 'contact.html')


import re

def mobile(request):
    MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)

    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        return True
    else:
        return False

def myfunction(request):
    if mobile(request):
        is_mobile = True
    else:
        is_mobile = False

    context = {
        'is_mobile': is_mobile,
    }
    return render(request, 'contact.html', context)
