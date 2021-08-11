from django.shortcuts import render, HttpResponseRedirect
from .models import Announcements, School
from register.decorators import teacher_required


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

    return render(request, "teacher_home_test.html", {"user": user, "school": school})


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
