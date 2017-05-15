# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import time
from star.models import Star
from photo import models as photo_models
# Create your views here.

def starit(request):
	context = {}
	try:
		filename = request.GET['file'].encode('utf-8')
	except:
		return render(request,'404.html')
	try:
		if request.META.has_key('HTTP_X_FORWARDED_FOR'):  
			ip =  request.META['HTTP_X_FORWARDED_FOR']  
		else:  
			ip = request.META['REMOTE_ADDR']
	except:
		ip = 'unknown'
	try:
		http_refer = request.META['HTTP_REFERER']  
	except:
		http_refer = 'no_referer'
	try:
		'''
		登录用户已赞
		'''
		username = request.session['username']
		star = Star.objects.filter(username=username,filename=filename)
		if len(star)>0:
			context['already_stared'] = 1
			return HttpResponseRedirect(http_refer)
	except:
		context['want_star_flag'] = 1
		return render(request,'login.html',context)
	
	

	star_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	star = Star()
	star.username = username
	star.filename = filename
	star.ip = ip
	star.time = star_time
	star.save()

	photo = photo_models.LivePhoto.objects.filter(filename=filename)[0]
	photo_star = photo.star
	photo.star = photo_star + 1
	photo.save()
	
	if http_refer == 'no_referer':
		return render(request,'404.html')
	else:
		return HttpResponseRedirect(http_refer)