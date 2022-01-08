
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from mycourses.forms.forms import UserRegistrationForm
from mycourses.models import Student, Subject, User, Teacher, Team, Lesson


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name',  'last_name', 'email']

# class UpdateProfileForm(forms.ModelForm):
#
#     class Meta:
#         model = Teacher


class CreateCourseForm(forms.Form):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    video_communication = forms.CharField(required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    log = forms.CharField(required=True,
                                          widget=forms.TextInput(attrs={'class': 'form-control'}))
    # class Meta:
    #     model = Team
    #     fields = ['id', 'name',  'video_communication', 'log', 'teacher']

class UpdateCourseForm(forms.ModelForm):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    video_communication = forms.CharField(required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    log = forms.CharField(required=True,
                                          widget=forms.TextInput(attrs={'class': 'form-control'}))


class CreateLessonForm(forms.ModelForm):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    name = forms.CharField(max_length=100,
                           required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=True,
                                          widget=forms.TextInput(attrs={'class': 'form-control'}))
    exercise = forms.CharField(required=True,
                          widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Lesson
        fields = '__all__'


class CreateStudentForm(forms.ModelForm):
    # id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    # name = forms.CharField(max_length=100,
    #                        required=True,
    #                        widget=forms.TextInput(attrs={'class': 'form-control'}))
    # description = forms.CharField(required=True,
    #                                       widget=forms.TextInput(attrs={'class': 'form-control'}))
    # exercise = forms.CharField(required=True,
    #                       widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = '__all__'

class UpdateLessonForm(forms.ModelForm):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    name = forms.CharField(max_length=100,
                           required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=True,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    exercise = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Lesson
        fields = '__all__'



class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


