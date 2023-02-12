from django.contrib import admin
from django.urls import path,include
from posts.views import IndexView,get_category,get_post

app_name = 'posts'

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('category<int:category_id>/',get_category,name='get_category'),
    path('post/<int:post_id>/',get_post,name='get_post'),

]