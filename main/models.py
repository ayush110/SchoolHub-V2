from django.db import models
from django_mysql.models import ListTextField

# Create your models here.


class Announcements(models.Model):
    announcement_title = models.CharField(max_length=200)
    announcement_content = models.TextField()


class Events(models.Model):
    event_title = models.CharField(max_length=200)
    event_content = models.TextField()
    event_date = models.CharField(max_length=200)
    # or we could use the actual datetime field event_date = models.DateTimeField()


class School(models.Model):
    name = models.CharField(
        max_length=255)
    announcements = ListTextField(base_field=models.TextField)

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
