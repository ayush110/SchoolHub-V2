from django.shortcuts import render, HttpResponseRedirect
from register.models import School

# Create your views here.


def createSchoolView(request):

    if request.method == "POST":
        name = request.POST.get('school_name')

        if name != "" and name != None:

            school = School.objects.create(name=name)
            school.save()

            return HttpResponseRedirect("/register/teacher-sign-up")

    return render(request, "create_school_test.html", {})
