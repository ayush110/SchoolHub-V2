from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from .forms import StudentSignUpForm
from .models import User


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'register/index_student.html'

    def get_context_data(self, **kwargs):
        print("GET CONTEXT DATA \n\n\n")
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        print("FORM VALID \n\n\n")
        if super().form_valid(form):
            user = form.save()
            login(self.request, user)
            return redirect('/student-home')
        else:
            return super().form_valid(form)


def StudentRegister(request):
    print("\n\n\n\n HIHIHIHI")
    if request.method == "POST":
        print("\n\n\n\n INNNNN")
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    else:
        form = StudentSignUpForm()

    return render(request, "register/index_student.html", {"form": form})
