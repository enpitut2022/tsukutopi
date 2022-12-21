from django import forms
from . models import Profile
 
class UserForm(forms.ModelForm):
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