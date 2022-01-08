from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView

from mycourses.forms.editprofile import  UpdateUserForm
from mycourses.forms.forms import *
from mycourses.models import *


class UserLogin(View):

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            user = authenticate(username=cd['username'], password=cd['password'])
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.is_teacher:
                        return redirect('home')
                    else:
                        return redirect('home')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')

    def get(self, request):
        form = LoginForm()
        return render(request, 'mycourses/bases/login.html', {'form': form})


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('home')


class Register(View):
    def get(self, request):
        user_form = UserRegistrationForm()
        return render(request, 'mycourses/bases/register.html', {'user_form': user_form})

    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.is_teacher = True
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            Teacher.objects.create(user=new_user)
        return redirect('home')

class Update(View):

    def get(self, request):
        user_form = UpdateUserForm(instance=request.user)
        # profile_form = UpdateProfileForm(instance=request.user.profile)
        # return render(request, 'mycourses/teacher/teacher_edit.html', {'user_form': user_form, 'profile_form': profile_form})
        return render(request, 'mycourses/teacher/teacher_edit.html',{'user_form': user_form})

    def post(self, request):
        user_form = UpdateUserForm(request.POST, instance=request.user)
        # profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        # if user_form.is_valid() and profile_form.is_valid():
        if user_form.is_valid():
            user_form.save()
            # profile_form.save()
            return redirect(to='home')

