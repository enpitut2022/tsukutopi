from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result', views.result, name="result"),
<<<<<<< HEAD:myapp/urls.py
=======
    path('input/',views.kakikomi, name='kakikomi'),
>>>>>>> origin/tk_layout2:tsukutopi/myapp/urls.py
]