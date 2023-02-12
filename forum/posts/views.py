from django.contrib import messages
from django.core.mail import message
from django.shortcuts import render
from django.views.generic import TemplateView
from commons.views import TitleMixinss
from posts.models import CategoryPosts,CommentsPosts,Posts
from posts.forms import CommentsForm
class IndexView(TitleMixinss,TemplateView):
    template_name = 'posts/index.html'
    title = 'Forum - Главная страница'
    paginate_by =3
    def get_context_data(self,**kwargs):
        context= super(IndexView, self).get_context_data()
        context['categories'] = CategoryPosts.objects.all()
        context['posts']=Posts.objects.filter(is_published=True)
        return context

def get_category(request,category_id):
    categories =CategoryPosts.objects.all()
    posts=Posts.objects.filter(category_id=category_id)
    category = CategoryPosts.objects.get(pk=category_id)
    context={
        'categories':categories,
        'posts':posts,
        'category':category,
    }
    return render(request,'posts/index.html',context)

def get_post(request,post_id):
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request,'Вы успешно отавили комментарий')
    else:
        form=CommentsForm()

    categories = CategoryPosts.objects.all()
    post = Posts.objects.get(pk=post_id)
    context = {
        'categories': categories,
        'post':post,
        'form':form
    }
    return render(request, 'posts/post.html', context)

