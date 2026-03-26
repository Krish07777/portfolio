from django.shortcuts import render, redirect
from .models import Profile, Project, Contact

def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        return redirect('home')

    return render(request, "home.html", {
        "profile": profile,
        "projects": projects
    })
