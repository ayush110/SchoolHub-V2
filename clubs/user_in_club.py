from register.models import Club


def student_in_club(user, id):
    club = Club.objects.get(id=id)

    if user.is_student and user.is_active:
        if user in club.members.all():
            return True
    return False


def teacher_in_club(user, id):
    club = Club.objects.get(id=id)

    if user.is_teacher and user.is_active:
        if user in club.members.all():
            return True
    return False


"""
def student_is_president_club(id):
"""
