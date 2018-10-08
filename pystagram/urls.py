"""pystagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path

from photos.views import hello
from photos.views import detail
from photos.views import create
from photos import views

from django.conf import settings
from django.conf.urls.static import static

#Djang에서 제공하는 인증 기능을 이용해서로그인, 로그아웃을 구현할 때 사용하는 클래스
from django.contrib.auth import views as auth_views


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
   # path(r'^hello/$', hello),
    re_path(r'^photos/(?P<pk>[0-9]+)/$', views.detail, name ='detail'),
    re_path(r'^photos/upload/$', views.create, name='create'),

    re_path(
        r'^accounts/login/',
        auth_views.LoginView.as_view(),
        name='login',
        kwargs={
            'template_name' : 'login.html',
        }
    ),
    re_path(
        r'^accounts/logout/',
        auth_views.LogoutView.as_view(),
        name='logout',
        kwargs={
            'next_page': settings.LOGIN_URL,
        }
    ),

]

urlpatterns += static('upload_files', document_root=settings.MEDIA_ROOT)