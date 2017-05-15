from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Comments(models.Model):
	filename = models.CharField(max_length=100,null=True)
	name = models.CharField(max_length=30,null=True)
	email = models.CharField(max_length=50,null=True)
	content = models.CharField(max_length=300,null=True)
	time = models.DateTimeField(null=True)
	isRegisted = models.IntegerField(default="1")