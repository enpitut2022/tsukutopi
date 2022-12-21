from django import forms

class Profile(forms.Form):
    key_number=forms.IntegerField()
    nickname=forms.CharField()
    major_sub = forms.IntegerField()
    circle=forms.CharField()
    hometown=forms.IntegerField()
    music=forms.IntegerField()
    ramen=forms.IntegerField()
    game=forms.IntegerField()
    anime=forms.IntegerField()
    movie=forms.IntegerField()
    sport=forms.IntegerField()