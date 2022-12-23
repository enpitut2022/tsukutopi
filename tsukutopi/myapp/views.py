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
    
    # major_list = ["総合学類", "人文学類", "比較文化学類", "日本語・日本文化学類", "社会学類", "国際総合学類", "教育学類", "心理学類", "障害科学類", "生物学類", "生物資源学類", "地球学類", "数学類", "物理学類", "化学類", "応用理工学類", "工学システム学類", "社会工学類", "情報科学類","情報メディア創生学類", "知識情報図書館学類", "医学類", "看護学類", "医療科学類", "体育専門学群", "芸術専門学群"]
    # hometown_list=["北海道", "青森県", "秋田県", "岩手県", "山形県", "宮城県", "福島県", "群馬県", "栃木県", "茨城県", "埼玉県", "東京都", "神奈川県", "千葉県", "新潟県", "長野県", "富山県", "石川県", "岐阜県", "静岡県", "山梨県", "愛知県", "福井県", "奈良県", "三重県", "和歌山県", "滋賀県", "大阪府", "京都府", "兵庫県", "鳥取県", "岡山県", "島根県", "広島県", "山口県", "香川県", "徳島県", "愛媛県", "高知県", "福岡県", "大分県", "佐賀県", "長崎県", "宮崎県", "熊本県", "鹿児島県", "沖縄県"]
    # music_list=["JPOP","洋楽","KPOP","HIPHOP", "クラシック", "EDM", "アニソン", "ロック"]
    # anime_list=["きらら系", "バトル系", "日常系", "スポーツ系", "なろう系", "ロボット系"]
    # movie_list=["アクション","恋愛","SF","コメディ","ホラー","サスペンス"]
    # ramen_list=["むじゃき","伊堂寺","真壁屋","鶏々","龍郎"]
    # sport_list=["野球","サッカー","バスケ","バレーボール","バドミントン","テニス"]#球技、武道、Non球技(武道以外)
    # game_list=["RPG", "FPS", "アクション", "育成", "ボードゲーム", "シューティング"]

    # for i in profile:
    #     i.major_sub = major_list[i.major_sub]
    context = {
        'profile':profile,
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