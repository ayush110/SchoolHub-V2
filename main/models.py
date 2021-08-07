from django.db import models
from django_mysql.models import ListTextField

# Create your models here.


class School(models.Model):
    name = models.CharField(
        max_length=255)

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Announcements(models.Model):
    announcement_title = models.CharField(max_length=200)
    announcement_content = models.TextField()

    school_announcements = models.ForeignKey(
        School, on_delete=models.CASCADE)
    club_announcements = models.ForeignKey(
        Club, on_delete=models.CASCADE)


class Events(models.Model):
    event_title = models.CharField(max_length=200)
    event_content = models.TextField()
    event_date = models.CharField(max_length=200)
    # or we could use the actual datetime field event_date = models.DateTimeField()

    school_events = models.ForeignKey(
        School, on_delete=models.CASCADE)
    club_events = models.ForeignKey(
        Club, on_delete=models.CASCADE)
