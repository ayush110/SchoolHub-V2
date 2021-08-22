from django.shortcuts import render, HttpResponseRedirect
from register.models import School, Announcements, Events
from register.decorators import teacher_required, student_required
from django.contrib.auth.decorators import login_required
from . import user_in_club


@login_required
@teacher_required
def school_delete_announcement(request, id, announcement_id):
    user = request.user

    if not user_in_club.teacher_in_club(user, id):
        return HttpResponseRedirect('/teacher-clubs')

    a = Announcements.objects.filter(id=announcement_id)
    a.delete()

    return HttpResponseRedirect(f'/teacher-view-club/{id}')


@login_required
@teacher_required
def school_delete_event(request, id, event_id):
    user = request.user

    if not user_in_club.teacher_in_club(user, id):
        return HttpResponseRedirect('/teacher-clubs')

    e = Events.objects.filter(id=event_id)
    e.delete()

    return HttpResponseRedirect(f'/teacher-view-club/{id}')


@login_required
@student_required
def school_delete_announcement_pres(request, id, announcement_id):
    user = request.user

    if not user_in_club.student_in_club(user, id):
        return HttpResponseRedirect('/student-clubs')

    a = Announcements.objects.filter(id=announcement_id)
    a.delete()

    return HttpResponseRedirect(f'/president-view-club/{id}')


@login_required
@student_required
def school_delete_event_pres(request, id, event_id):
    user = request.user

    if not user_in_club.student_in_club(user, id):
        return HttpResponseRedirect('/student-clubs')

    e = Events.objects.filter(id=event_id)
    e.delete()

    return HttpResponseRedirect(f'/president-view-club/{id}')
