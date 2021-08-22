from django.shortcuts import render, HttpResponseRedirect
from register.models import Announcements, Club
from register.decorators import teacher_required
from django.contrib.auth.decorators import login_required
from . import user_in_club

# Create your views here.


@login_required
@teacher_required
def create_club(request):
    user = request.user
    school = user.school

    if request.method == 'POST':

        if 'back' in request.POST:
            return HttpResponseRedirect('/teacher-clubs')

        else:
            name = request.POST.get('title')
            description = request.POST.get('description')

            if school.club_set.filter(name=name):
                return render(request, "create_club_test.html", {"user": user, "school": school, 'sameError': True})

            school.club_set.create(
                name=name, description=description)
            club = school.club_set.filter(name=name)[0]
            club.members.add(user, through_defaults={
                'isPresident': False, 'isCreater': True})

            return HttpResponseRedirect('/teacher-clubs')

    return render(request, "create_club_test.html", {"user": user, "school": school, 'sameError': False})


@login_required
@teacher_required
def teacher_clubs(request):
    user = request.user
    school = user.school

    clubs = Club.objects.filter(school=school)
    yourClubs = []
    otherClubs = []
    yourClubs2 = True

    for club in clubs:
        if user in club.members.all():
            yourClubs.append(club)
        else:
            otherClubs.append(club)

    if request.method == 'POST':

        if 'yourClubs' in request.POST:
            clubs = yourClubs
            yourClubs2 = True

        elif 'otherClubs' in request.POST:
            clubs = otherClubs
            yourClubs2 = False

        elif 'addClub' in request.POST:
            return HttpResponseRedirect('/create-club')

        for club in clubs:
            if f'view{club.id}' in request.POST:
                return HttpResponseRedirect(f'/teacher-view-club/{club.id}')

            elif f'join{club.id}' in request.POST:
                pass

    else:
        clubs = yourClubs

    return render(request, "clubs_test.html", {"user": user, "school": school, "clubs": clubs, "yourClubs2": yourClubs2})


@login_required
@teacher_required
def teacher_view_club(request, id):

    if not user_in_club.teacher_in_club(id):
        return HttpResponseRedirect('/teacher-clubs')

    user = request.user
    school = user.school
    club = Club.objects.get(id=id)

    if request.method == 'POST':

        if 'back' in request.POST:
            return HttpResponseRedirect('/teacher-clubs')

        elif 'create_announcement' in request.POST:
            return HttpResponseRedirect(f'/create-club-announcement/{id}')

        elif 'create_event' in request.POST:
            return HttpResponseRedirect(f'/create-club-event/{id}')

        else:
            for event in club.events_set.all():
                if f'e{event.id}' in request.POST:
                    return HttpResponseRedirect(f'/teacher-club-event-zoom-in/{club.id}/{event.id}')

            for announcement in club.announcements_set.all():
                if f'a{announcement.id}' in request.POST:
                    return HttpResponseRedirect(f'/teacher-club-announcement-zoom-in/{club.id}/{announcement.id}')

    announcements = club.announcements_set.all()
    events = club.events_set.all()
    members = club.members.all()

    if len(announcements) > 8:
        announcements = announcements[:8]
    if len(events) > 4:
        events = events[:4]
    if len(members) > 3:
        members = members[:3]

    passcode = club.passcode

    return render(request, "view_club_test.html", {"user": user, "school": school, "announcements": announcements, "events": events, "members": members, "passcode": passcode, "club": club})


@login_required
@teacher_required
def teacher_club_event_zoom_in(request, id, event_id):
    if not user_in_club.teacher_in_club(id):
        return HttpResponseRedirect('/teacher-clubs')
    user = request.user
    school = user.school
    club = Club.objects.get(id=id)

    if request.method == 'POST':
        if 'back' in request.POST:
            return HttpResponseRedirect(f'/teacher-view-club/{id}')

        if 'delete' in request.POST:
            return HttpResponseRedirect(f'/delete-club-event/{id}/{event_id}')

    event = club.events_set.get(id=event_id)

    return render(request, 'teacher_club_event_zoom_in_test.html', {"user": user, "school": school, "event": event, "club": club})


@login_required
@teacher_required
def teacher_club_announcement_zoom_in(request, id, announcement_id):
    if not user_in_club.teacher_in_club(id):
        return HttpResponseRedirect('/teacher-clubs')
    user = request.user
    school = user.school
    club = Club.objects.get(id=id)

    if request.method == 'POST':
        if 'back' in request.POST:
            return HttpResponseRedirect(f'/teacher-view-club/{id}')

        if 'delete' in request.POST:
            return HttpResponseRedirect(f'/delete-club-announcement/{id}/{announcement_id}')

    announcement = club.announcements_set.get(id=announcement_id)

    return render(request, 'teacher_club_announcement_zoom_in_test.html', {"user": user, "school": school, "announcement": announcement, "club": club})


@login_required
@teacher_required
def create_club_announcement(request, id):
    if not user_in_club.teacher_in_club(id):
        return HttpResponseRedirect('/teacher-clubs')
    user = request.user
    school = user.school
    club = Club.objects.get(id=id)

    if request.method == 'POST':
        if 'back' in request.POST:
            return HttpResponseRedirect(f'/teacher-view-club/{club.id}')

        else:
            title = request.POST.get('title')
            description = request.POST.get('description')

            club.announcements_set.create(
                announcement_title=title, announcement_content=description)

            return HttpResponseRedirect(f'/teacher-view-club/{club.id}')

    return render(request, "create_club_announcement_test.html", {"user": user, "school": school, "club": club})


@login_required
@teacher_required
def create_club_event(request, id):
    if not user_in_club.teacher_in_club(id):
        return HttpResponseRedirect('/teacher-clubs')
    user = request.user
    school = user.school
    club = Club.objects.get(id=id)

    if request.method == 'POST':
        if 'back' in request.POST:
            return HttpResponseRedirect(f'/teacher-view-club/{club.id}')

        else:
            title = request.POST.get('title')
            description = request.POST.get('description')
            date = request.POST.get('date')

            club.events_set.create(
                event_title=title, event_content=description, event_date=date)

            return HttpResponseRedirect(f'/teacher-view-club/{club.id}')

    return render(request, "create_club_event_test.html", {"user": user, "school": school, "club": club})
