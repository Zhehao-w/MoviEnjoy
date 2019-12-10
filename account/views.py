from django.shortcuts import render
from account.forms import UserForm, UserProfileInfoForm, UserUpdateForm, UserProfileInfoUpdateForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.views.generic import (
    View, TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView)
from . import models


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about_us(request):
    return render(request, 'about_us.html')


@login_required
def special(request):
    return HttpResponse("Your are logged in, nice.")


@login_required  # anything require login to see, add this line
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(UserForm.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'account/registration.html', {'user_form': user_form,
                                                         'profile_form': profile_form,
                                                         'registered': registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('Account not active')

        else:
            print("someone try to login and failed.")
            print(f'Username {username} and password {password}')
            return HttpResponse("invalid login details supplied")

    else:
        return render(request, 'account/login.html', {})


@login_required
def profile(request):
    return render(request, 'account/profile.html')


def update_profile(request):
    updated = False

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileInfoUpdateForm(
            request.POST, request.FILES, instance=request.user.userprofileinfo)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            # return HttpResponseRedirect(reverse('index'))

        updated = True

    else:
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileInfoUpdateForm(
            request.POST, instance=request.user.userprofileinfo)

    context = {'u_form': u_form, 'p_form': p_form, "updated": updated}
    return render(request, 'account/profile_update.html', context)
