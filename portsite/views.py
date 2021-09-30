from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Project
from .models import Quote
from .models import Log

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

def breathe(request):
	quotes = Quote.objects.all()
	return render(request, 'breathe.html',  {'quotes' : quotes})

def candy(request):
	logs = Log.objects.all()
	return render(request, 'candy.html')

def test1(request):
	logs = Log.objects.all()
	return render(request, 'test1.html', {'logs' : logs})

def message(request):
	return render(request, 'message.html')
