from django.db import models
from django.contrib.auth.models import User

class Folder(models.Model):
	name = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User)

	def __str__(self):
		return self.name

class File(models.Model):
	Folder = models.ForeignKey(Folder,on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	link = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'Files'

	def __str__(self):
		return self.name[:50] + "..."