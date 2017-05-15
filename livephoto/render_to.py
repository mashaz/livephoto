# -*- coding: utf-8 -*-
 
from django.shortcuts import render
from photo import models 
from django.http import HttpResponse,HttpResponseRedirect
from comments import models as cmodels
from star import models as star_models
from random import shuffle
def photos(request):
	photo_list = models.LivePhoto.objects.all()
	context = {}
	context['photo_list'] = photo_list
	return render(request, 'photo-list.html',context)

def index_page(request):
	try:
		page = int(request.GET['page'].encode('utf-8'))
	except:
		page = 1

	photo_list = models.LivePhoto.objects.all() #[2:5]
	page_sum = len(photo_list)
	page_list = []
	for i in range(1,int(page_sum/12+2)):
		page_list.append(i)
	# photo_list = photo_list[::-1] # reverse
	# photo_list = shuffle(photo_list) # random
	if page == 1:
		photo_list = photo_list[0:12]
	else:
		try:
			photo_list = photo_list[(12*(page-1)):(12*page)]
		except:
			photo_list = photo_list[(12*(page-1)):(len(page_list))]
	context = {}
	context['page_list'] = page_list
	context['photo_list'] = photo_list
	#print len(photo_list)
	return render(request, 'index.html',context)

def upload_page(request):

	try:
	    request.session['username']
	except:
		context = {}
		context['post_flag'] = 1
		return render(request, 'login.html',context)

	return render(request, 'upload.html')

def single_page(request):
	try:
		
		filename = request.GET['file'].encode('utf-8')
	except:
		return HttpResponse('error')
	try:
		photo = models.LivePhoto.objects.filter(filename=filename)[0]
		comments = cmodels.Comments.objects.filter(filename=filename)
	except:
		return HttpResponse('error')
	try:
		stars = star_models.Star.objects.filter(filename=filename)
		star_sum =  len(stars)
	except:
		star_sum = 0
	context = {}
	star_last_five = []
	for i  in range(len(stars)-1,len(stars)-4,-1):
		try:
			star_last_five.append(stars[i])
		except:
			break
	try:
		username = request.session['username']
	except:
		username = 'anonymous'
	if username!='anonymous':
		is_star_sum = star_models.Star.objects.filter(filename=filename,username=username)
		if  len(is_star_sum) > 0:
			context['is_star'] = 1
	context['stars'] = star_last_five
	context['star_sum'] = star_sum
	context['photo'] = photo
	context['comments'] = comments
	return render(request, 'single-page.html',context)