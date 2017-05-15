from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Star(models.Model):
	filename = models.CharField(max_length=100,null=True)
	username = models.CharField(max_length=30,null=True)
	time = models.DateTimeField(null=True)
	ip = models.CharField(max_length=30,null=True)
	