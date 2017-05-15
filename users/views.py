#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from users.models import User
from django import forms
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

#定义表单模型
class UserForm(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    password = forms.CharField(label='密码：',widget=forms.PasswordInput())

#登录

def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                request.session['username'] = username
                return HttpResponseRedirect('/')
            else:
                user_by_email = User.objects.filter(email__exact = username,password__exact = password)
                if user_by_email:
                    request.session['username'] = user_by_email[0].username
                    return HttpResponseRedirect('/')
                else:
                    context = {}
                    context['invid'] = 'invid'
                    return render(request, 'login.html', context)

    return render_to_response('login.html')

def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return HttpResponseRedirect('/')

def is_username_legal(username):
    if len(username) < 4 :
        return 0
    elif username == 'anonymous':
        return 0
    elif len(username) > 20 :
        return 0
    elif ' ' in username:
        return 0
    elif '.' in username:
        return 0
    elif ',' in username:
        return 0
    elif '-' in username:
        return 0
    else:
        return 1
def is_password_legal(password):
    if len(password) < 6 :
        return 0
    else:
        return 1
def register(request):
    if request.method == 'POST':
        context = {}
        username = request.POST['username'].encode('utf-8')
        if is_username_legal(username) == 0:
            context['illegal_username'] = 1
            return render(request,'register.html',context)
        password = request.POST['password'].encode('utf-8')
        if is_password_legal(password) == 0:
            context['illegal_password'] = 1
            return render(request,'register.html',context)
        email = request.POST['email'].encode('utf-8')
        user = User.objects.filter(username=username)

        
        if len(user)==0:
            user = User()
            user.username = username
            user.password = password
            user.email = email
            user.save()
            # todo 判断username email
            
            context['register_flag'] = 'register succeed'
            context['register_username'] = username
            return render(request,'login.html',context)

        elif  user[0].username == username:
            context['exist_username'] = 1
            return render(request,'register.html',context)

        else:
            user = User.objects.filter(email=email)
            if user[0].email == email:
                context['exist_email'] = 1
                return render(request,'register.html',context)
           
    else:
        try:
            del request.session['username']
        except:
            pass
        return render_to_response('register.html')
def info(request):
    try:
        username = request.session['username']
    except:
        return HttpResponseRedirect('/account/register')
    context = {}
    user = User.objects.filter(username=username)[0]
    context['user'] = user
    return render(request,'userinfo.html',context)

def change_info(request):
    username = request.session['username']
    user = User.objects.filter(username=username)
    try:
        email = request.POST['email'].encode('utf-8')
        if len(email)< 2 or email == '':
            raise no_email
        is_change_email = 1
    except:
        is_change_email = 0

    try:
        password1 = request.POST['password1'].encode('utf-8')
        password2 = request.POST['password2'].encode('utf-8')
        if password1 == password2:
            password = password1
        else:
            return HttpResponse('密码不一致')
        if len(password)< 6 or password == '':
            raise no_password
        is_change_pwd = 1
    except:
        is_change_pwd = 0

    user = User.objects.filter(username=username)[0]
    if is_change_email :
        user.email = email
    if is_change_pwd :
        user.password = password
    user.save()
    return HttpResponseRedirect('/account/logout')
def watch_profile(request):
    try:    
        username = request.GET['username'].encode('utf-8')
    except:
        return  render(request,'404.html')
    try:
        user_list = User.objects.filter(username=username)
    except:
        return HttpResponseRedirect('/')
    if len(user_list) == 0 :
        return HttpResponseRedirect('/')
    user = user_list[0]
    context = {}
    context['user'] = user
    return render(request,'profile.html',context)
