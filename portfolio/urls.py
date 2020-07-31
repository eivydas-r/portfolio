from django.conf.urls import url
from django.contrib import admin
from portsite import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', views.home, name = 'home'),
	url(r'^resume/', views.resume, name = 'resume'),
	url(r'^about/', views.about, name = 'about'),
	url(r'^projects/', views.projects, name = 'projects'),
	url(r'^contact/', views.contact, name = 'contact'),
	url(r'^breathe', views.breathe, name = 'breathe'),
	url(r'^breathe/', views.breathe, name = 'breathe'),

	url(r'^test1/', views.test1, name = 'test1'),
]
