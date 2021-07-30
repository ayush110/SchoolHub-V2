from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from .forms import StudentSignUpForm
from .models import User


"""def StudentSignUpViewFunc(request):

    if request.method == "POST":
        print("\n\n\n\n\n\n\n")
        form = StudentSignUpForm(request)
        if form.is_valid():
            form.save()
            return redirect("/student-home")

    else:
        form = StudentSignUpForm()

    return render(request, "register/register.html", {"form": form})"""


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'register/register.html'

    def get_context_data(self, **kwargs):
        print("\n\n\nget context data\n\n\n\n")
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        print("\n\n\n\n\n\n\n")
        if super().form_valid(form):
            user = form.save()
            login(self.request, user)
            return redirect('/student-home')
        else:
            return super().form_valid(form)
