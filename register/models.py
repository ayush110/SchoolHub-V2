import random
import string
from django.contrib.auth.models import AbstractUser
from django.db import models
#from main.models import School


def generate_random_passcode():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


class School(models.Model):
    name = models.CharField(
        max_length=255)

    def __str__(self):
        return self.name


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE)


class Club(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    passcode = models.CharField(
        default=generate_random_passcode, max_length=30)
    members = models.ManyToManyField(User, through='Member')

    def __str__(self):
        return self.name


class Member(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isPresident = models.BooleanField(default=False)
    isCreator = models.BooleanField(default=False)
    isOwner = models.BooleanField(default=False)


class Announcements(models.Model):
    announcement_title = models.CharField(max_length=200)
    announcement_content = models.TextField()

    school_announcements = models.ForeignKey(
        School, on_delete=models.CASCADE, null=True)
    club_announcements = models.ForeignKey(
        Club, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.announcement_title


class Events(models.Model):
    event_title = models.CharField(max_length=200)
    event_content = models.TextField()
    event_date = models.CharField(max_length=200)
    # or we could use the actual datetime field event_date = models.DateTimeField()

    school_events = models.ForeignKey(
        School, on_delete=models.CASCADE, null=True)
    club_events = models.ForeignKey(
        Club, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.event_title
