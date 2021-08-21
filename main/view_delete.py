from django.shortcuts import render, HttpResponseRedirect
from register.models import School, Announcements, Events
from register.decorators import teacher_required
from django.contrib.auth.decorators import login_required


@teacher_required
def school_delete_announcement(request, id):

    a = Announcements.objects.filter(id=id)
    a.delete()

    return HttpResponseRedirect('/teacher-home')


@teacher_required
def school_delete_event(request, id):

    e = Events.objects.filter(id=id)
    e.delete()

    return HttpResponseRedirect('/teacher-school-event')
