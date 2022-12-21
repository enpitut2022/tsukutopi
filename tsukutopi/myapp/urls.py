from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result', views.result, name="result"),
    
    #ユーザの詳細情報を表示する処理を呼び出す
    #ユーザの登録フォームを呼び出す
    path('create', views.showCreateUserForm, name='showCreateUserForm'),
    #ユーザ登録する処理を呼び出す
    path('add', views.addUser, name='addUser'),

]