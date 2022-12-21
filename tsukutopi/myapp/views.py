from django.shortcuts import render
from .models import Profile
from django.db.models import Q
from .forms import UserForm
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
    major_list = ["総合学類", "情報メディア創生学類", "人文学類", "比較文化学類", "日本語・日本文化学類", "社会学類", "国際総合学類", "教育学類", "心理学類", "障害科学類", "生物学類", "生物資源学類", "地球学類", "数学類", "物理学類", "化学類", "応用理工学類", "工学システム学類", "社会工学類", "情報科学類", "知識情報図書館学類", "医学類", "看護学類", "医療科学類", "体育専門学群", "芸術専門学群"]
    for i in profile:
        i.major_sub = major_list[i.major_sub]
    context = {
        'profile':profile,
        'major_list': major_list
    }
    

    return render(request, 'myapp/result.html', context)

#～～～～～～～～～～～～～～～～～
# 新規登録フォームHTMLへ返す
def showCreateUserForm(request):
    #フォームを変数にセット
    form = UserForm()
 
    context = {
        'userForm':form,
    }
 
    #detail.htmlへデータを渡す
    return render(request, 'myapp/create.html',context)

# フォームから受取ったデータをDBに登録する
def addUser(request):
    #リクエストがPOSTの場合
    if request.method == 'POST':
        #リクエストをもとにフォームをインスタンス化
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            userForm.save()
 
    #登録後、全件データを抽出
    profile_data = Profile.objects.all()
    context = {
        'msg': '現在の利用状況',
        'userinfo': profile_data,
        'count':profile_data.count,
    }
 
    #user.htmlへデータを渡す
    return render(request, 'myapp/users.html',context)