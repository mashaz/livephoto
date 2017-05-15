# -*- coding:utf-8 -*-

from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from photo.models import LivePhoto
from django import forms
from django.http import HttpResponse
from users.models import User 
import random
import string
import time
# Create your views here.
# def add_photo(request):
# 	filename = request.GET['filename'].encode('utf-8')
# 	try:
# 		uploader = request.GET['uploader'].encode('utf-8')
# 	except:
# 		uploader = 'anonymous'
#  	livephoto = LivePhoto()
# 	livephoto.filename = filename
# 	livephoto.uploader = uploader
# 	livephoto.save()
# 	return HttpResponse('ok')
def upload(request):
	try:
		uploader = request.session['username']
	except:
		uploader = 'anonymous'
	try:
		title = request.POST['title'].encode('utf-8')
	except:
		title = 'untitled'
	try:
		location = request.POST['location'].encode('utf-8')
	except:
		location = 'unknown'
	try:
		describtion = request.POST['describtion'].encode('utf-8')
	except:
		describtion = 'This is a LivePhoto!'
	try:
		jpgfile = request.FILES['jpg-file']
		movfile = request.FILES['mov-file']
	except:
		return HttpResponse('nofile')

	slist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
	filename = string.join(random.sample(slist, 20)).replace(" ","")
	file_path = 'static/assets/' + str(filename)
	jpg_f = open('%s.jpg'%(file_path),'wb+') 
	jpg_f.write(jpgfile.read())  
	jpg_f.close()
	mov_f = open('%s.mov'%(file_path),'wb+') 
	mov_f.write(movfile.read())  
	mov_f.close()
	upload_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

 	livephoto = LivePhoto()
	livephoto.filename = filename
	livephoto.uploader = uploader
	livephoto.location = location
	livephoto.describe = describtion
	livephoto.time = upload_time
	livephoto.name = title
	livephoto.save()
	try:
		user = User.objects.filter(username=uploader)[0]
		user.upload_sum += 1
		user.save()
	except:
		pass
	return HttpResponseRedirect('/')
def delete(request):
	try:
		username = request.session['username']
		filename = request.GET['fid'].encode('utf-8')
	except:
		return HttpResponseRedirect('/')
	try:
		photo = LivePhoto.objects.filter(filename=filename)[0]
		user = User.objects.filter(username=username)[0]
	except:
		return HttpResponseRedirect('/')
	photo.delete()
	user.upload_sum -= 1
	user.save()
	return HttpResponseRedirect('/')

def user_photo(request):
	try:
		username = request.GET['user'].encode('utf-8')
	except:
		HttpResponseRedirect('/')
	photo_list = LivePhoto.objects.filter(uploader=username)
	print len(photo_list)
	context = {}
	context['photo_list'] = photo_list

	return render(request,'user-upload.html',context)


	