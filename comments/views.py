# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from comments.models import Comments
import time
# Create your views here.

def comment_post(request):
	comment_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	try:
		filename = request.POST['filename'].encode('utf-8')
	except:
		HttpResponse('error')
	try:
		username = request.session['username']
		content = request.POST['content'].encode('utf-8')
		if len(content)  < 2:
			return render(request,'404.html')
		comment = Comments()
		comment.filename = filename
		comment.name = username
		comment.content = content
		comment.isRegisted = 1
		comment.time = comment_time
		comment.save()
		file
	except:
		try:
			username = request.POST['username'].encode('utf-8')
			email = request.POST['email'].encode('utf-8')
			content = request.POST['content'].encode('utf-8')
			print len(username)
			if len(username) < 2 or len(email) <2  or len(content)  < 2:
				return render(request,'404.html')
			username += '(游客)'
			comment = Comments()
			comment.filename = filename
			comment.name = username
			comment.content = content
			comment.email = email
			comment.isRegisted = 0
			comment.time = comment_time
			comment.save()

		except:
			return render(request,'404.html')
	return HttpResponseRedirect('/detail?file=%s'%(filename))