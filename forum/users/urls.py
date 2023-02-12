from django.contrib import admin
from django.urls import path,include
from users.views import UserLoginView,UserRegisterView,profile

app_name = 'users'

urlpatterns = [
    path('login/',UserLoginView.as_view(),name='login'),
    #path('register/',UserRegisterView.as_view(),name='register')
    path('profile/',profile,name='profile')
]