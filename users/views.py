from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout
from .forms import UserRegistrationForm, LoginForm, ProfileForm, UserForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def registration(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created")
            return redirect("login")
    return render(request,"users/registration.html",{"form":form})


def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect("home")
        else:
            messages.error(request,"Invalid Username or Password")
    return render(request,"users/login.html",{"form":form})


def logout(request):
    auth_logout(request)
    return redirect("login")

@login_required
def profile(request):
    user = request.user
    user_form = UserForm(instance=user)
    profile_form = ProfileForm(instance=user.userprofile)
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES,instance=user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("home")

    return render(request,"users/profile.html",{"user_form":user_form,"profile_form":profile_form})