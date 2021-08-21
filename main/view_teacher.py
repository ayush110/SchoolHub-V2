from django.shortcuts import render, HttpResponseRedirect
from register.models import Announcements, School, Events
from register.decorators import teacher_required
from django.contrib.auth.decorators import login_required


@login_required
@teacher_required
def teacher_home(request):
    user = request.user
    school = user.school

    if request.method == 'POST':

        if "create_announcement" in request.POST:
            return HttpResponseRedirect('/school-create-announcement')

        for announcement in school.announcements_set.all():
            if str(announcement.id) in request.POST:
                return HttpResponseRedirect('/school-zoom-in-announcement/' + str(announcement.id))

    # make a limit on the size of the announcement

    announcements = reversed(school.announcements_set.all())

    return render(request, "teacher_home_test.html", {"user": user, "school": school, "announcements": announcements})


@login_required
@teacher_required
def school_announcement_zoom_in(request, id):
    user = request.user
    school = user.school

    if request.method == 'POST':
        if 'back' in request.POST:
            return HttpResponseRedirect('/teacher-home')

        elif str(id) in request.POST:
            return HttpResponseRedirect('/school-delete-announcement/' + str(id))

    announcement = Announcements.objects.filter(id=id)
    announcement = announcement[0]

    return render(request, "teacher_announcement_zoom_in_test.html", {"school": school, "announcement": announcement})


@login_required
@teacher_required
def school_create_announcement(request):
    user = request.user
    school = user.school

    if request.method == 'POST':
        if 'back' in request.POST:
            return HttpResponseRedirect('/teacher-home')

        elif 'create' in request.POST:
            title = request.POST.get('title')
            description = request.POST.get('description')

            school.announcements_set.create(
                announcement_title=title, announcement_content=description)

            return HttpResponseRedirect('/teacher-home')

    return render(request, "create_announcement_test.html", {"school": school})


@login_required
@teacher_required
def teacher_school_event(request):
    user = request.user
    school = user.school

    if request.method == 'POST':

        if "create_event" in request.POST:
            return HttpResponseRedirect('/school-create-event')

        for event in school.events_set.all():
            if str(event.id) in request.POST:
                return HttpResponseRedirect('/school-zoom-in-event/' + str(event.id))

    events = reversed(school.events_set.all())

    return render(request, "teacher_school_event_test.html", {"user": user, "school": school, "events": events})


@login_required
@teacher_required
def school_create_event(request):
    user = request.user
    school = user.school

    if request.method == 'POST':
        if 'back' in request.POST:
            return HttpResponseRedirect('/teacher-school-event')

        elif 'create' in request.POST:
            title = request.POST.get('title')
            description = request.POST.get('description')
            date = request.POST.get('date')

            school.events_set.create(
                event_title=title, event_content=description, event_date=date)

            return HttpResponseRedirect('/teacher-school-event')

    return render(request, "create_event_test.html", {"user": user, "school": school})


@login_required
@teacher_required
def school_event_zoom_in(request, id):
    user = request.user
    school = user.school

    if request.method == 'POST':
        if 'back' in request.POST:
            return HttpResponseRedirect('/teacher-school-event')

        elif str(id) in request.POST:
            return HttpResponseRedirect('/school-delete-event/' + str(id))

    event = Events.objects.filter(id=id)
    event = event[0]

    return render(request, "teacher_event_zoom_in_test.html", {"school": school, "user": user, "event": event})
