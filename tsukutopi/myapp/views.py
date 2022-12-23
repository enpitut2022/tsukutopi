from django.shortcuts import render, redirect
from .models import Profile
from django.db.models import Q
from myapp.forms import Profileforms
from django.http import HttpResponse
# Create your views here.

def index(request):
    profile = Profile.objects.all()
    context = {
        'profile':profile
    }

    return render(request, 'myapp/template.html', context)

def result(request):
    profile = Profile.objects.filter(Q(key_number=202088888)|Q(key_number=202099999))
    profile_match = Profile.objects.filter(Q(key_number=202088888)|Q(key_number=202099999))
    profile_all = Profile.objects.all()
    share_point=[]
    print(profile[0].nickname)
    object_items = vars(profile[0])
    # print(object_items["key_number"])
    for i in object_items.keys():
        if vars(profile[0])[i] == vars(profile[1])[i]:      
            share_point.append(vars(profile[0])[i])
        
    # major_list = ["総合学類", "情報メディア創生学類", "人文学類", "比較文化学類", "日本語・日本文化学類", "社会学類", "国際総合学類", "教育学類", "心理学類", "障害科学類", "生物学類", "生物資源学類", "地球学類", "数学類", "物理学類", "化学類", "応用理工学類", "工学システム学類", "社会工学類", "情報科学類", "知識情報図書館学類", "医学類", "看護学類", "医療科学類", "体育専門学群", "芸術専門学群"]
    # for i in profile:
    #     i.major_sub = major_list[i.major_sub]
    context = {
        'profile':profile,
        'share_point':share_point,
        # 'major_list': major_list,
        'profile_all':profile_all
    }
    

    return render(request, 'myapp/result.html', context)

def kakikomi(request):
    f = Profileforms()
    if request.method =='POST':
        profileform = Profileforms(request.POST)
        if profileform.is_valid():
            profileform.save()
            return redirect('index')

    return render(request, 'myapp/input_profile.html', {'form1': f} )