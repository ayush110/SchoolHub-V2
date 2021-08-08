from django.shortcuts import render, HttpResponseRedirect
from .forms import CreateSchool
from .models import School

# Create your views here.


def createSchoolView(request):
    if request.method == "POST":
        form = CreateSchool(request.POST)

        if form.is_valid():
            name = form.cleaned_data["school_name"]
            school = School(name=name)
            school.save()

            return HttpResponseRedirect("/login")

    else:
        form = CreateSchool()

    return render(request, "create_school.html", {"form": form})
