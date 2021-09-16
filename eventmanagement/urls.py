"""eventmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from core import views 
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('events/',views.events,name='events'),
    path('eventregister/',views.eventregister,name='eventregister'),
    path('bharatanatyam/',views.bharatanatyam,name='bharatanatyam'),
    path('painting/',views.painting,name='painting'),
    path('mohiniyattam/',views.mohiniyattam,name='mohiniyattam'),
    path('mime/',views.mime,name='mime'),
    path('groupsong/',views.groupsong,name='groupsong'),
    path('groupdance/',views.groupdance,name='groupdance'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('signup/',views.user_signup,name='signup'),
    
]
