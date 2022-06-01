from unicodedata import name
from django.urls import path, include # New
from django.views.generic import TemplateView # New
from landing import views


urlpatterns = [
    path('',views.index ,name='index'),
    path('news',views.news ,name='news'),
    path('newsDetail/<int:id>', views.newsDetail,name='newsDetail'),
    # path('newsForm',views.newsForm ,name='newsForm'),
    path('newsForm/', views.AddPostView.as_view(), name='newsForm'),
    path('logout',views.log_out ,name='log_out'),
    path('login',views.login ,name='login'),
    path('loginForm',views.loginForm ,name='loginForm'),
    path('registerForm',views.registerForm ,name='registerForm'),
    path('register',views.register ,name='register'),
    path('knowledge',views.knowledge,name='knowledge'),
]