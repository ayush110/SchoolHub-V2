from django.shortcuts import render, HttpResponseRedirect
from register.models import Announcements, Club, Member
from register.decorators import student_required
from django.contrib.auth.decorators import login_required
from . import user_in_club
from . import order_members


@login_required
@student_required
def president_view_club(request, id):

    user = request.user
    school = user.school

    if not user_in_club.student_in_club(user, id):
        return HttpResponseRedirect('/student-clubs')
    club = Club.objects.get(id=id)

    member = Member.objects.filter(club=club, user=user)[0]
    if not member.isPresident:
        return HttpResponseRedirect(f'/student-view-club/{id}')

    if request.method == 'POST':

        if 'back' in request.POST:
            return HttpResponseRedirect('/student-clubs')

        elif 'create_announcement' in request.POST:
            return HttpResponseRedirect(f'/create-club-announcement-pres/{id}')

        elif 'create_event' in request.POST:
            return HttpResponseRedirect(f'/create-club-event-pres/{id}')

        elif 'member_list' in request.POST:
            return HttpResponseRedirect(f'/student-member-list/{id}')

        else:
            for event in club.events_set.all():
                if f'e{event.id}' in request.POST:
                    return HttpResponseRedirect(f'/pres-club-event-zoom-in/{club.id}/{event.id}')

            for announcement in club.announcements_set.all():
                if f'a{announcement.id}' in request.POST:
                    return HttpResponseRedirect(f'/pres-club-announcement-zoom-in/{club.id}/{announcement.id}')

    announcements = club.announcements_set.all()
    events = club.events_set.all()
    members = Member.objects.filter(club=club)
    members = order_members.members_list(members)

    if len(announcements) > 8:
        announcements = announcements[:8]
    if len(events) > 4:
        events = events[:4]
    if len(members) > 3:
        members = members[:3]

    announcements = reversed(announcements)
    events = reversed(events)

    passcode = club.passcode

    return render(request, "view_club_test.html", {"user": user, "school": school, "announcements": announcements, "events": events, "members": members, "passcode": passcode, "club": club})


@login_required
@student_required
def create_club_announcement_pres(request, id):
    user = request.user
    school = user.school
    if not user_in_club.student_in_club(user, id):
        return HttpResponseRedirect('/student-clubs')
    club = Club.objects.get(id=id)

    member = Member.objects.filter(club=club, user=user)[0]
    if not member.isPresident:
        return HttpResponseRedirect(f'/student-view-club/{id}')

    if request.method == 'POST':
        if 'back' in request.POST:
            return HttpResponseRedirect(f'/president-view-club/{club.id}')

        else:
            title = request.POST.get('title')
            description = request.POST.get('description')

            club.announcements_set.create(
                announcement_title=title, announcement_content=description)

            return HttpResponseRedirect(f'/president-view-club/{club.id}')

    return render(request, "create_club_announcement_test.html", {"user": user, "school": school, "club": club})


@login_required
@student_required
def create_club_event_pres(request, id):
    user = request.user
    school = user.school
    if not user_in_club.student_in_club(user, id):
        return HttpResponseRedirect('/student-clubs')
    club = Club.objects.get(id=id)

    member = Member.objects.filter(club=club, user=user)[0]
    if not member.isPresident:
        return HttpResponseRedirect(f'/student-view-club/{id}')

    if request.method == 'POST':
        if 'back' in request.POST:
            return HttpResponseRedirect(f'/president-view-club/{club.id}')

        else:
            title = request.POST.get('title')
            description = request.POST.get('description')
            date = request.POST.get('date')

            club.events_set.create(
                event_title=title, event_content=description, event_date=date)

            return HttpResponseRedirect(f'/president-view-club/{club.id}')

    return render(request, "create_club_event_test.html", {"user": user, "school": school, "club": club})


@login_required
@student_required
def president_club_event_zoom_in(request, id, event_id):
    user = request.user
    school = user.school
    if not user_in_club.student_in_club(user, id):
        return HttpResponseRedirect('/student-clubs')
    club = Club.objects.get(id=id)

    member = Member.objects.filter(club=club, user=user)[0]
    if not member.isPresident:
        return HttpResponseRedirect(f'/student-view-club/{id}')

    if request.method == 'POST':
        if 'back' in request.POST:
            return HttpResponseRedirect(f'/president-view-club/{id}')

        if 'delete' in request.POST:
            return HttpResponseRedirect(f'/delete-club-event-pres/{id}/{event_id}')

    event = club.events_set.get(id=event_id)

    return render(request, 'teacher_club_event_zoom_in_test.html', {"user": user, "school": school, "event": event, "club": club})


@login_required
@student_required
def president_club_announcement_zoom_in(request, id, announcement_id):
    user = request.user
    school = user.school
    if not user_in_club.student_in_club(user, id):
        return HttpResponseRedirect('/student-clubs')
    club = Club.objects.get(id=id)

    member = Member.objects.filter(club=club, user=user)[0]
    if not member.isPresident:
        return HttpResponseRedirect(f'/student-view-club/{id}')

    if request.method == 'POST':
        if 'back' in request.POST:
            return HttpResponseRedirect(f'/president-view-club/{id}')

        if 'delete' in request.POST:
            return HttpResponseRedirect(f'/delete-club-announcement-pres/{id}/{announcement_id}')

    announcement = club.announcements_set.get(id=announcement_id)

    return render(request, 'teacher_club_announcement_zoom_in_test.html', {"user": user, "school": school, "announcement": announcement, "club": club})
