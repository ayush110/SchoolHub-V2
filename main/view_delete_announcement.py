from django.shortcuts import render, HttpResponseRedirect
from .models import School, Announcements
from register.decorators import teacher_required


@teacher_required
def school_delete_announcement(request, id):

    a = Announcements.objects.filter(id=id)
    a.delete()

    return HttpResponseRedirect('/teacher-home')
