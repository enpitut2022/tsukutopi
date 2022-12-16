from django.shortcuts import render
from .models import Profile
# Create your views here.

def index(request):
    profile = Profile.objects.all()
    context = {
        'profile':profile
    }

    return render(request, 'myapp/template.html', context)

def result(request):
    profile = Profile.objects.all()
    context = {
        'profile':profile
    }

    return render(request, 'myapp/result.html', context)

