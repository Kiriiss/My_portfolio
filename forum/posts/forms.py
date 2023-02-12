from django import forms
from posts.models import CommentsPosts
class CommentsForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control-4', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control-4', 'placeholder': 'Введите фамилию'}))
    posts_image = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    context= forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control','rows':4, 'placeholder': 'Введите текст отзыва'}))
    class Meta:
        model = CommentsPosts
        fields =('first_name','last_name','posts_image','context')