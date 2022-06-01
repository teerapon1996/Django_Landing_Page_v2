from django.shortcuts import render, redirect
from landing.models import *
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from django.views.generic.list import ListView
from .forms import PostForm

class AddPostView(ListView):
    model = News
    def get(self, request):
        form = PostForm()
        context = {
        'page': 'newsForm',
        'form': form
        }
        return render(request, 'newsForm.html', context)
    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            descriptions = form.cleaned_data['descriptions']
            image = form.cleaned_data['image']
            news = News.objects.create(
                    title=title,
                    descriptions=descriptions,
                    image=image,
                    )
            news.save()
            messages.info(request,'+Add News, Successful !')
            return redirect('/news')
        return redirect('/newsForm')
# def newsAdd(request,):
    
#     title_name = request.POST['title_name']
#     desc = request.POST['desc']
#     image = request.FILES['image']

#     if title_name == "" or desc == "" or image =="" :
#         messages.info(request,f'กรุณากรอกข้อมูลให้ครบทุกช่อง')
#         return redirect('/newsForm')
#     else:
#         news = News.objects.create(
#                 name=title_name,
#                 desc=desc,
#                 image=image,
#                 )
#         news.save()
#         messages.info(request,'+Add News, Successful !')
#         return redirect('/news')


def index(request):
    data = News.objects.all().order_by('-created')[:4]
    context = {
        'newss':data,
        'page': 'index'
    }
    return render(request,'index.html', context)

def news(request):
    data = News.objects.all().order_by('-created')
    
    context = {
        'newss':data,
        'last_news': News.objects.all().order_by('-created').first(),
        'page': 'news',
    }
    return render(request,'news.html', context)      

def newsDetail(request, id):
    data = News.objects.get(id=id)
    news={'news':data}
    return render(request,'newsDetail.html', news)

# def newsForm(request):
#     context = {
#         'page': 'newsForm'
#     }
#     if request.user.is_superuser:
#         return render(request,'newsForm.html', context)
#     elif request.user.is_authenticated:
#         messages.info(request,'The user does not have permission.')
#         return redirect('/')
#     else :
#         messages.info(request,'The user does not have permission.')
#         return redirect('/')
def loginForm(request):
    context = {
        'page': 'loginForm'
    }
    if request.user.is_authenticated or request.user.is_superuser:
        return redirect('/') 
    else:
        return render(request,'loginForm.html', context)

def log_out(request):
    logout(request)
    messages.info(request,'ออกจากระบบเรียบร้อย')
    return redirect('/') 

def knowledge(request):
    context = {
        'page': 'knowledge'
    }
    return render(request,'knowledge.html', context )

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    #check username
    user = auth.authenticate(username=username,password=password)
    print(user)
    if user is not None :
        auth.login(request,user)
        return redirect('/')  
    else:
        messages.info(request,'ไม่พบผู้ใช้งานในระบบ')
        return redirect('/loginForm') 

def registerForm(request):
    return render(request,'registerForm.html') 

def register(request):
    username=request.POST['username']
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    password=request.POST['password']
    repassword=request.POST['repassword']

    if password == repassword :
        if username == "" or firstname == "" or lastname =="" or email =="" or password=="" or repassword=="" :
            messages.info(request,f'กรุณากรอกข้อมูลให้ครบทุกช่อง')
            return redirect('/registerForm')
        else:    
            if User.objects.filter(username=username).exists():
                messages.info(request,f'Username "{username}" นี้ถูกใช้งานแล้ว')
                return redirect('/registerForm')
            elif User.objects.filter(email=email).exists():
                messages.info(request,f'Email "{email}" นี้ถูกใช้งานแล้ว')
                return redirect('/registerForm')
            elif len(password) <= 7 :
                messages.info(request,f'Password ต้องมีตัวอักษรหรือตัวเลขอย่างน้อย 8 ตัว')
                return redirect('/registerForm') 
            else:
                user=User.objects.create(
                username=username,
                email=email,
                first_name=firstname,
                last_name=lastname,
                )
                user.set_password(password)
                user.save()
                messages.info(request,'ลงทะเบียน เรียบร้อยแล้ว !')
                return redirect('/')
    else:
        messages.info(request,'Password ไม่ตรงกัน')
        return redirect('/registerForm')
