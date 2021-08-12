from django.contrib.auth.models import AbstractUser
from django.db import models
from main.models import School


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
