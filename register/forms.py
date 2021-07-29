from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Student, User

class StudentSignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        return user
