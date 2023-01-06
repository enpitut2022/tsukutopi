from django import forms
from .models import Profile
from .formlist import *

class Profileforms(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('key_number','nickname','major_sub','circle','hometown','music','ramen','game','anime','movie','sport')
        labels={
           'key_number':'学籍番号',
           'nickname':'ニックネーム',
           'major_sub':'所属学類',
           'circle':'所属サークル',
           'hometown':'出身地',
           'music':'好きな音楽',
           'ramen':'好きなラーメン屋',
           'game':'好きなゲーム',
           'anime':'好きなアニメ',
           'movie':'好きな映画',
           'sport':'好きなスポーツ',
           }

class ProfileRadioForm(forms.Form):
    key_number = forms.IntegerField(label='学籍番号')
    nickname = forms.CharField(label='ニックネーム')
    major_sub = forms.ChoiceField(choices=MAJORS, label='専攻', widget=forms.widgets.RadioSelect)
    circle = forms.CharField(label='サークル')
    hometown = forms.ChoiceField(choices=PREFECTURES, label='出身', widget=forms.widgets.RadioSelect)
    music = forms.ChoiceField(choices=MUSICLIST, label='好きな音楽', widget=forms.widgets.RadioSelect)
    ramen = forms.ChoiceField(choices= RAMENLIST, label='好きなラーメン', widget=forms.widgets.RadioSelect)
    game = forms.ChoiceField(choices= GAMELIST, label='好きなゲーム', widget=forms.widgets.RadioSelect)
    anime = forms.ChoiceField(choices= ANIMELIST, label='好きなアニメ', widget=forms.widgets.RadioSelect)
    movie = forms.ChoiceField(choices= MOVIELIST, label='好きな映画', widget=forms.widgets.RadioSelect)
    sport = forms.ChoiceField(choices= SPORTLIST, label='好きなスポーツ', widget=forms.widgets.RadioSelect)