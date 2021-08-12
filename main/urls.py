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
from . import view_create_school
from . import view_teacher
from . import view_delete


urlpatterns = [
    path("create-school", view_create_school.createSchoolView, name="create-school"),
    path("teacher-home", view_teacher.teacher_home, name="teacher-home"),
    path("school-delete-announcement/<int:id>", view_delete.school_delete_announcement,
         name="school-delete-announcement"),
    path("school-zoom-in-announcement/<int:id>", view_teacher.school_announcement_zoom_in,
         name="school-zoom-in-announcement"),
    path("school-create-announcement", view_teacher.school_create_announcement,
         name="school-create-announcement"),
    path("school-delete-event/<int:id>", view_delete.school_delete_event,
         name="school-delete-event"),
    path("teacher-school-event", view_teacher.teacher_school_event,
         name="teacher-school-event"),
    path("school-zoom-in-event/<int:id>", view_teacher.school_event_zoom_in,
         name="school-zoom-in-event"),
    path("school-create-event", view_teacher.school_create_event,
         name="school-create-event"),

]
