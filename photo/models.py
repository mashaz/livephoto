from __future__ import unicode_literals

from django.db import models

# Create your models here.
class LivePhoto(models.Model):
	filename = models.CharField(max_length=100,null=True)
	uploader = models.CharField(max_length=30,null=True)
	name = models.CharField(max_length=30,null=True)
	describe = models.CharField(max_length=200,null=True)
	time = models.DateTimeField(null=True)
	location = models.CharField(max_length=50,null=True)
	star = models.IntegerField(default='0')

