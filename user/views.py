from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from crud.models import Blog
from user.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from user.forms import SignUpForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import UserProfile
from django.core import serializers


# Create your views here.
def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user =request.user
            #userprofile=UserProfile.objects.get(user_id=current_user.id)
            #request.session['userimage'] = userprofile.image.url
            #request.session['currency'] = userprofile.currency.code

            # Redirect to a success page.
            messages.success(request, "Welcome back")
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,"Login Error !! Username or Password is incorrect")
            return HttpResponseRedirect('/login')
    # Return an 'invalid login' error message.

    return render(request, 'login.html', {})


def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() #completed sign up
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Create data in profile table for user
            current_user = request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.image="images/users/user.png"
            data.cover_image="images/cover.jpg"
            data.save()
            messages.success(request, 'Your account has been created! Please save your location details')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect('/signup')

    form = SignUpForm()
    context = {
               'form': form,
               }
    return render(request, 'register.html', context)


def logout_func(request):
    logout(request)
    messages.success(request, 'You are successfully logged out')
    return HttpResponseRedirect('/')


def userprofile(request):
    blog=Blog.objects.filter(user_id=request.user.id)
    return render(request,'userprofile.html',{'blog':blog})


@login_required(login_url='/login') # Check login
@csrf_exempt
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) # request.user is user  data
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return HttpResponseRedirect('/user/myprofile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile) #"userprofile" model -> OneToOneField relatinon with user
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'user_update.html', context)


