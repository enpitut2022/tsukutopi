from django.shortcuts import render, redirect
from .models import Profile
from django.db.models import Q
from myapp.forms import ProfileRadioForm
# Create your views here.

def index(request):
    profile = Profile.objects.all()
    context = {
        'profile':profile
    }

    return render(request, 'myapp/template.html', context)

def result(request):
    profile = Profile.objects.filter(Q(key_number=202012154)|Q(key_number=202011111))
    profile_all = Profile.objects.all()
    share_point=[]
    # print(profile[0].nickname)
    object_items = vars(profile[0])
    # print(object_items["key_number"])
    for i in object_items.keys():
        if vars(profile[0])[i] == vars(profile[1])[i]:      
            share_point.append(vars(profile[0])[i])
        
    context = {
        # 'profile':profile,
        'share_point':share_point,
        'profile_all':profile_all
    }
    

    return render(request, 'myapp/result.html', context)

def kakikomi(request):
    if request.method =='POST':
        profile = Profile(
        key_number = request.POST['key_number'],
        nickname = request.POST['nickname'],
        major_sub = request.POST['major_sub'],
        circle = request.POST['circle'],
        hometown = request.POST['hometown'],
        music = request.POST['music'],
        ramen = request.POST['ramen'],
        game = request.POST['game'],
        anime = request.POST['anime'],
        movie = request.POST['movie'],
        sport = request.POST['sport']
        )
        profile.save()
        return redirect('index')
    else:
        profileform = ProfileRadioForm()
        context = {
            'form': profileform
        }
    return render(request, 'myapp/input_profile.html', context)