"""
URL configuration for ethics_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from articles.views import article_list, contact_view, article_detail, video_list, about_view
from articles.views import community_view, add_post
from django.contrib.auth import views as auth_views


# Simple inline home_view
def home_view(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Homepage
    path('articles/', article_list, name='article_list'),
    path('article/<int:article_id>/', article_detail, name='article_detail'),
    path('contact/', contact_view, name='contact'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('videos/', video_list, name='video_list'),
    path('community/', community_view, name='community'),
    path('community/add/', add_post, name='add_post'),
     path('about/', about_view, name='about'),
]
