from django.shortcuts import render, redirect
from .forms import UserCreateForm, SignUpForm

# Create your models here.

def signup_view(request):
    if request.method == 'GET':
        form = SignUpForm
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        form = SignUpForm(request.POST)

        if form.is_valid():
            # 회원가입 처리
            instance = form.save()
            return redirect('index')
        else:
            return redirect('accounts:signup')