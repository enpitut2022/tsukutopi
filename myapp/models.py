from django.db import models

# Create your models here.
class Profile(models.Model):
    key_number=models.IntegerField(max_length=9,primary_key=True)
    nickname=models.CharField(max_length=50)
    major_sub = models.IntegerField(max_length=2)
    circle=models.CharField(max_length=50)
    hometown=models.IntegerField(max_length=2)
    music=models.IntegerField(max_length=2)
    ramen=models.IntegerField(max_length=2)
    game=models.IntegerField(max_length=2)
    anime=models.IntegerField(max_length=2)
    movie=models.IntegerField(max_length=2)
    sport=models.IntegerField(max_length=2)
    
