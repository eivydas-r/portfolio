from django.db import models

# Create your models here.
class Project(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	project_date = models.DateField(blank=True, null=True)

	#project = this.objects.get(id=1)
	#if project.id == 1:
	details = models.ManyToManyField('Details', blank=True)
	#else:
	#	print("test")
	# image
	# link/video

class Details(models.Model):
	detail_id = models.PositiveIntegerField(default=0)
	order_number = models.PositiveIntegerField(default=0)
	description = models.TextField()

	def __str__(self): # string representation of this model
		try:
			#print("Not found, detail_id: " + str(self.detail_id))
			project = Project.objects.get(id=self.detail_id)
			print("detail_id: " + str(self.detail_id) + " ... project id: " + str(project.id))
			
			if self.detail_id == project.id:
				return "Detail " + str(self.detail_id) + ": " + str(self.description) + str(project.id)
			else:
				return "No details available"
		except:
			print("Not found")
			return "error"#"Not found, detail_id: " + str(self.detail_id) + "project id: " + str(project.id)


		#image = models.ImageField()

#d1 = Details(detail_id=1,order_number=1)
#p1 = Project()
#p1.save()
#p1.name = "Test1"
