from django.contrib import admin
from posts.models import *

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):

    list_display = ('title','is_published','category')
    list_editable = ('is_published',)

@admin.register(CategoryPosts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(CommentsPosts)