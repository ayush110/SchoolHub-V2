"""SchoolHub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.shortcuts import render, HttpResponseRedirect


def redirect1(request, w="", w2=""):
    if request.user:
        if request.user.is_student:
            return HttpResponseRedirect("/student-home")
        else:
            return HttpResponseRedirect("/teacher-home")

    else:
        return HttpResponseRedirect("/login")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", include('register.urls')),
    path("", include('main.urls')),
    path('', include("django.contrib.auth.urls")),
    path("", redirect1)
]
