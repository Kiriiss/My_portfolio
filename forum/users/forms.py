from django import forms
from users.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm

class UserLoginForm(AuthenticationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Введите email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Введите пароль'}))
    class Meta:
        model = User
        fields=('email','password',)

class Registrationform(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите фамилию'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль еще раз'}))
    class Meta:
        model=User
        fields = ('first_name','last_name','email', 'password1','password2',)

class ChangeForm(UserChangeForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control-4', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control-4', 'placeholder': 'Введите фамилию'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control-4', 'placeholder': 'Введите email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control-4', 'placeholder-4': 'Введите пароль'}))
    posts_image = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control-4'}))

    class Meta:
        model=User
        fields = ('first_name','last_name','email','password','photo')
