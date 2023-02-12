from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from commons.views import TitleMixinss
from users.forms import UserLoginForm,ChangeForm

class UserLoginView(TitleMixinss,LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('posts:index')
    title = 'Forum - авторизация'


class UserRegisterView():
    pass

def profile(request):
    if request.method == 'POST':
        form = ChangeForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = ChangeForm
    return render(request,'users/profile.html',{'form':form})
