from django.shortcuts import render

from .models import Member


# Create your views here.
def home(request):
    members = Member.objects.all()
    data = {
        "members": members,
    }
    return render(request, 'pages/home.html', data)


def about(request):
    members = Member.objects.all()
    data = {
        "members": members,
    }
    return render(request, 'pages/about.html', data)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')