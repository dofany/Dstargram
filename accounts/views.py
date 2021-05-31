# 회원가입
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)

        if signup_form.is_valid():
            user_instance = signup_form.save(commit=False)
            user_instance.set_password(signup_form.cleaned_data['password'])
            user_instance.save()
            return render(request,'accounts/signup_complete.html',{'username':user_instance.username})
    else:
        signup_form = SignUpForm()
    return render(request, 'accounts/signup.html',{'form':signup_form.as_p})
