from django.db import models

class CategoryPosts(models.Model):
    objects = None
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title


class Posts(models.Model):
    objects = None
    title=models.CharField(max_length=50)
    content= models.TextField()
    image = models.ImageField(upload_to='image',blank=True)
    time = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(CategoryPosts,on_delete=models.PROTECT,null=True)

class CommentsPosts(models.Model):
    first_name=models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    posts_image = models.ImageField(upload_to='posts_image',blank=True)
    context = models.TextField(null=True)
    is_published = models.BooleanField(default=False)
    



