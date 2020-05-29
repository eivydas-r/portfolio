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
