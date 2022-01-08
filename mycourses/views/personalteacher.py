from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView, TemplateView

from mycourses.forms.editprofile import *
from mycourses.forms.forms import *
from mycourses.models import *


class CreateCourse(View):
    def get(self, request):
        if request.user.is_authenticated:
            # print(Teacher.objects.get(user=request.user.id))
            user_form = CreateCourseForm()
            return render(request, 'mycourses/teacher/create_course.html', {'user_form': user_form})

    def post(self, request):
        if request.user.is_authenticated:
            user_form = CreateCourseForm(request.POST)
            # profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
            # if user_form.is_valid() and profile_form.is_valid():
            if user_form.is_valid():
                cd = user_form.cleaned_data
                print(cd['name'])
                Team.objects.create(name=cd['name'],video_communication=cd['video_communication'], log=cd['log'], teacher=Teacher.objects.get(user=request.user.id))
                return HttpResponse('Молодца')

# class UpdateCourse(View):
#
#     def get(self, request):
#         if request.user.is_authenticated:
#             print(Teacher.objects.get(user=request.user.id))
#             user_form = UpdateCourseForm()
#             return render(request, 'mycourses/teacher/create_course.html', {'user_form': user_form})
#
#     def post(self, request):
#         if request.user.is_authenticated:
#             user_form = UpdateCourseForm(request.POST)
#             # profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
#             # if user_form.is_valid() and profile_form.is_valid():
#             if user_form.is_valid():
#
#                 return HttpResponse('Молодца')



class ShowCourses(ListView):
    model = Team
    template_name = 'mycourses/teacher/show_courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        user = self.request.user
        print(self.request.user.id)
        context = Team.objects.filter(teacher=user.id)
        return context

class ShowCourse(View):

    def get(self, request, course_id):
        # news_item = News.objects.get(pk=news_id)
        course_item = get_object_or_404(Team, pk=course_id)
        lessons = Lesson.objects.filter(team=course_id)
        students = Student.objects.filter(team=course_id)
        print(lessons)
        return render(request, 'mycourses/teacher/show_course.html', {"course_item": course_item, "lessons": lessons, "students": students})

class ShowLesson(View):
    def get(self, request, course_id, lesson_id):
        lesson_item = get_object_or_404(Lesson, pk=lesson_id)
        return render(request, 'mycourses/teacher/show_lesson.html', {"lesson_item": lesson_item, "course_id": course_id,  "lesson_id": lesson_id})

class UpdateLesson(View):
    def get(self, request, course_id, lesson_id):
        lesson_item = get_object_or_404(Lesson, pk=lesson_id)
        user_form = UpdateLessonForm(instance=lesson_item)
        user_form.fields['team'].queryset = Team.objects.filter(pk=course_id)
        return render(request, 'mycourses/teacher/edit_lesson.html', {'user_form': user_form})

    def post(self, request, course_id, lesson_id):
        lesson_item = get_object_or_404(Lesson, pk=lesson_id)
        user_form = UpdateLessonForm(lesson_item, request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect(to='show_lesson')

class CreateLesson(View):

    def get(self, request, course_id):
        if request.user.is_authenticated:
            user_form = CreateLessonForm()
            print(course_id)
            # news_item = get_object_or_404(Team, pk=course_id)
            print(Team.objects.filter(teacher=request.user.id))
            user_form.fields['team'].queryset = Team.objects.filter(pk=course_id)
            return render(request, 'mycourses/teacher/create_lesson.html', {'user_form': user_form})

    def post(self, request, course_id):
        if request.user.is_authenticated:
            user_form = CreateLessonForm(request.POST)
            user_form.fields['team'].queryset = Team.objects.filter(pk=course_id)
            if user_form.is_valid():
                user_form.save()
                return HttpResponse('Молодца')


class ShowStudent(View):

    def get(self, request, course_id, student_id):
        # news_item = News.objects.get(pk=news_id)
        student_item = get_object_or_404(Student, pk=student_id)

        return render(request, 'mycourses/teacher/show_student.html', {"lesson_item": student_item, "course_id": course_id, "student_id": student_id})

class UpdateStudent(View):
    def get(self, request, course_id, student_id):
        student_item = get_object_or_404(User, pk=student_id)
        user_form = UpdateUserForm(instance=student_item)
        student_form = UpdateStudentForm(instance=student_item)
        student_form.fields['user'].queryset = User.objects.filter(pk=student_id)
        student_form.fields['team'].queryset = Team.objects.filter(pk=course_id)
        return render(request, 'mycourses/teacher/edit_student.html', {'user_form': user_form, 'student_form': student_form })

    def post(self, request, course_id, student_id):
        # student_item = get_object_or_404(Student, pk=student_id)
        user_form = UpdateStudentForm(request.POST)
        student_form = UpdateStudentForm(request.POST)
        if user_form.is_valid():
            user_form.save()
        if student_form.is_valid():
            student_form.save()
        return redirect(to='show_student', course_id=course_id, student_id=student_id)


class CreateStudent(View):
    def get(self, request, course_id):
        if request.user.is_authenticated:
            user_form = UserRegistrationForm()
            return render(request, 'mycourses/teacher/create_student.html', {'user_form': user_form})

    def post(self, request, course_id):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.is_student = True
            new_user.set_password(user_form.cleaned_data['password'])
            # user_form.fields['team'].queryset = Team.objects.filter(pk=course_id)
            new_user.save()
            Student.objects.create(user=new_user, team=Team.objects.get(pk=course_id))
            return HttpResponse('Молодца')



