
def members_list(members):

    owner = []
    teachers = []
    presidents = []
    general_members = []

    for member in members:
        if member.isOwner:
            owner.append(member)

        elif member.isCreator:
            teachers.append(member)

        elif member.isPresident:
            presidents.append(member)

        else:
            general_members.append(member)

    result = []
    result.extend(owner)
    result.extend(teachers)
    result.extend(presidents)
    result.extend(general_members)

    return result
