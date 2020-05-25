from django.db import models

# Create your models here.
class Project(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	project_date = models.DateField()
	details = models.ManyToManyField('Details', blank=True)
	# image
	# link/video

class Details(models.Model):
	detail_id = models.PositiveIntegerField(default=0)
	order_number = models.PositiveIntegerField(default=0)
	description = models.TextField()
	#image = models.ImageField()
