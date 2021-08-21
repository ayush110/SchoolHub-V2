from django.shortcuts import render, HttpResponseRedirect
from register.models import Announcements, School, Events
from register.decorators import student_required
from django.contrib.auth.decorators import login_required


@login_required
@student_required
def student_home(request):
    user = request.user
    school = user.school

    if request.method == 'POST':

        for announcement in school.announcements_set.all():
            if str(announcement.id) in request.POST:
                return HttpResponseRedirect('/student-school-zoom-in-announcement/' + str(announcement.id))

    # make a limit on the size of the announcement

    announcements = reversed(school.announcements_set.all())

    return render(request, "student_home_test.html", {"user": user, "school": school, "announcements": announcements})


@login_required
@student_required
def student_school_zoom_in_announcement(request, id):
    user = request.user
    school = user.school

    if request.method == 'POST':
        if 'back' in request.POST:
            return HttpResponseRedirect('/student-home')

    announcement = Announcements.objects.filter(id=id)
    announcement = announcement[0]

    return render(request, "student_announcement_zoom_in_test.html", {"school": school, "announcement": announcement})


@login_required
@student_required
def student_school_event(request):
    user = request.user
    school = user.school

    if request.method == 'POST':
        for event in school.events_set.all():
            if str(event.id) in request.POST:
                return HttpResponseRedirect('/student-school-zoom-in-event/' + str(event.id))

    events = reversed(school.events_set.all())

    return render(request, "student_school_event_test.html", {"user": user, "school": school, "events": events})


@login_required
@student_required
def student_school_event_zoom_in(request, id):
    user = request.user
    school = user.school

    if request.method == 'POST':
        if 'back' in request.POST:
            return HttpResponseRedirect('/student-school-event')

    event = Events.objects.filter(id=id)
    event = event[0]

    return render(request, "student_event_zoom_in_test.html", {"school": school, "user": user, "event": event})
