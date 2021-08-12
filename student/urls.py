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
from django.urls import path
from . import view_student


urlpatterns = [
    path("student-home", view_student.student_home, name="student-home"),
    path("student-school-zoom-in-announcement/<int:id>",
         view_student.student_school_zoom_in_announcement, name="student-school-zoom-in-announcement"),
    path("student-school-event", view_student.student_school_event,
         name="student-school-event"),
    path("student-school-zoom-in-event/<int:id>",
         view_student.student_school_event_zoom_in, name="student-school-zoom-in-event")
]
