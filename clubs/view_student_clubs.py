from django.shortcuts import render, HttpResponseRedirect
from register.models import Announcements, Club, Member
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
    user = request.user
    school = user.school

    if not user_in_club.student_in_club(user, id):
        return HttpResponseRedirect('/student-clubs')

    club = Club.objects.get(id=id)

    member = Member.objects.filter(club=club, user=user)[0]
    if member.isPresident:
        print(id, end="\n\n\n")
        return HttpResponseRedirect(f'/president-view-club/{id}')

    if request.method == 'POST':

        if 'back' in request.POST:
            return HttpResponseRedirect('/student-clubs')

        elif 'member_list' in request.POST:
            return HttpResponseRedirect(f'/student-member-list/{id}')

        """else:
            for event in club.events_set.all():
                if f'e{event.id}' in request.POST:
                    return HttpResponseRedirect(f'/student-club-event-zoom-in/{club.id}/{event.id}')

            for announcement in club.announcements_set.all():
                if f'a{announcement.id}' in request.POST:
                    return HttpResponseRedirect(f'/student-club-announcement-zoom-in/{club.id}/{announcement.id}')"""

    announcements = club.announcements_set.all()
    events = club.events_set.all()
    members = Member.objects.filter(club=club)

    if len(announcements) > 8:
        announcements = announcements[:8]
    if len(events) > 4:
        events = events[:4]
    if len(members) > 3:
        members = members[:3]

    return render(request, 'student_view_club_test.html', {"user": user, "school": school, "announcements": announcements, "events": events, "members": members})


@login_required
@student_required
def join_club(request, id):
    user = request.user
    school = user.school
    club = Club.objects.get(id=id)

    if request.method == 'POST':
        if 'back' in request.POST:
            return HttpResponseRedirect('/student-clubs')

        passcode = request.POST.get('passcode')

        if club.passcode == passcode:
            club.members.add(user, through_defaults={})
            return HttpResponseRedirect(f'/student-view-club/{club.id}')
        else:
            return render(request, 'student_join_club.html', {"user": user, "school": school, "error": True, "club": club})

    return render(request, 'student_join_club.html', {"user": user, "school": school, "error": False, "club": club})


@login_required
@student_required
def member_list(request, id):
    user = request.user
    school = user.school
    if not user_in_club.student_in_club(user, id):
        return HttpResponseRedirect('/student-clubs')

    club = Club.objects.get(id=id)
    members = Member.objects.filter(club=club)

    if request.method == 'POST':

        if 'back' in request.POST:
            return HttpResponseRedirect(f'/student-view-club/{id}')

    #members = club.members.all()

    return render(request, 'student_member_list_test.html', {"user": user, "school": school, "club": club, "members": members})
