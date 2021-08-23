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
from . import view_student_clubs
from . import view_clubs
from . import view_delete
from . import view_president_clubs


urlpatterns = [
    path('teacher-clubs', view_clubs.teacher_clubs, name="teacher-clubs"),
    path('create-club', view_clubs.create_club, name="create-club"),
    path('teacher-view-club/<int:id>',
         view_clubs.teacher_view_club, name="teacher-view-club"),
    path('create-club-announcement/<int:id>',
         view_clubs.create_club_announcement, name="create-club-announcement"),
    path('create-club-event/<int:id>',
         view_clubs.create_club_event, name="create-club-event"),
    path('teacher-club-event-zoom-in/<int:id>/<int:event_id>',
         view_clubs.teacher_club_event_zoom_in, name="teacher-club-event-zoom-in"),
    path('teacher-club-announcement-zoom-in/<int:id>/<int:announcement_id>',
         view_clubs.teacher_club_announcement_zoom_in, name="teacher-club-announcement-zoom-in"),
    path('delete-club-announcement/<int:id>/<int:announcement_id>',
         view_delete.school_delete_announcement, name="teacher-club-announcement-zoom-in"),
    path('delete-club-event/<int:id>/<int:event_id>',
         view_delete.school_delete_event, name="teacher-club-event-zoom-in"),
    path('member-list/<int:id>', view_clubs.member_list,
         name="member-list"),
    path('join-club/<int:id>', view_clubs.join_club,
         name="join-club"),

    path('student-clubs', view_student_clubs.student_clubs_home, name="student-clubs"),
    path('student-view-club/<int:id>', view_student_clubs.student_view_club,
         name="student-view-club"),
    path('student-join-club/<int:id>', view_student_clubs.join_club,
         name="student-join-club"),
    path('student-member-list/<int:id>', view_student_clubs.member_list,
         name="student-member-list"),
    path('student-club-event-zoom-in/<int:id>/<int:event_id>',
         view_student_clubs.student_school_zoom_in_event, name="student-club-event-zoom-in"),
    path('student-club-announcement-zoom-in/<int:id>/<int:ann_id>',
         view_student_clubs.student_school_zoom_in_announcement, name="student-club-announcement-zoom-in"),


    path('president-view-club/<int:id>', view_president_clubs.president_view_club,
         name="president-view-club"),
    path('create-club-announcement-pres/<int:id>',
         view_president_clubs.create_club_announcement_pres, name="create-club-announcement-pres"),
    path('create-club-event-pres/<int:id>',
         view_president_clubs.create_club_event_pres, name="create-club-event-pres"),
    path('delete-club-announcement-pres/<int:id>/<int:announcement_id>',
         view_delete.school_delete_announcement_pres, name="delete-club-announcement-pres"),
    path('delete-club-event-pres/<int:id>/<int:event_id>',
         view_delete.school_delete_event_pres, name="delete-club-event-pres"),
    path('pres-club-event-zoom-in/<int:id>/<int:event_id>',
         view_president_clubs.president_club_event_zoom_in, name="pres-club-event-zoom-in"),
    path('pres-club-announcement-zoom-in/<int:id>/<int:announcement_id>',
         view_president_clubs.president_club_announcement_zoom_in, name="pres-club-announcement-zoom-in"),
]
