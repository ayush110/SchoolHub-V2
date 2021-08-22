from django.shortcuts import render, HttpResponseRedirect
from register.models import Announcements, Club
from register.decorators import student_required
from django.contrib.auth.decorators import login_required
from . import user_in_club


@login_required
@student_required
def student_clubs_home(request):
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

        for club in clubs:
            if f'view{club.id}' in request.POST:
                return HttpResponseRedirect(f'/student-view-club/{club.id}')

            elif f'join{club.id}' in request.POST:
                return HttpResponseRedirect(f'/student-join-club/{club.id}')

    else:
        clubs = yourClubs

    return render(request, 'student_clubs_home_test.html', {"user": user, "school": school, "clubs": clubs, "yourClubs2": yourClubs2})


@login_required
@student_required
def student_view_club(request, id):

    if not user_in_club.student_in_club(id):
        return HttpResponseRedirect('/student-clubs')

    user = request.user
    school = user.school
    club = Club.objects.get(id=id)

    if request.method == 'POST':

        if 'back' in request.POST:
            return HttpResponseRedirect('/student-clubs')

        """else:
            for event in club.events_set.all():
                if f'e{event.id}' in request.POST:
                    return HttpResponseRedirect(f'/student-club-event-zoom-in/{club.id}/{event.id}')

            for announcement in club.announcements_set.all():
                if f'a{announcement.id}' in request.POST:
                    return HttpResponseRedirect(f'/student-club-announcement-zoom-in/{club.id}/{announcement.id}')"""

    announcements = club.announcements_set.all()
    events = club.events_set.all()
    members = club.members.all()

    if len(announcements) > 8:
        announcements = announcements[:8]
    if len(events) > 4:
        events = events[:4]
    if len(members) > 3:
        members = members[:3]

    return render(request, 'student_view_club_test.html', {"user": user, "school": school, "announcements": announcements, "events": events, "members": members})


def join_club(request, id):
    user = request.user
    school = user.school

    if request.method == 'POST':
        if 'back' in request.POST:
            return HttpResponseRedirect('/student-clubs')

        passcode = request.POST.get('passcode')
        club = Club.objects.get(id=id)

        if club.passcode == passcode:
            club.members.add(user, through_defaults={})
            return HttpResponseRedirect(f'/student-view-club/{club.id}')
        else:
            return render(request, 'student_join_club.html', {"user": user, "school": school, "error": True})

    return render(request, 'student_join_club.html', {"user": user, "school": school, "error": False})
