from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView

from mycourses.forms.forms import *
from mycourses.models import *


class HomeCourses(ListView):
    model = Lesson
    template_name = 'mycourses/bases/course.html'
    context_object_name = 'courses'


class CourseByCategory(ListView):
    model = Subject
    template_name = 'mycourses/course.html'
    context_object_name = 'courses'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return Subject.objects.filter(category_id=self.kwargs['category_id'])


class HomeView(View):
    context = {
        'countLesson': Lesson.objects.count(),
        'countStudent': Student.objects.count(),
        'countTeacher': Teacher.objects.count(),
    }

    def get(self, request):
        print(request.user)
        if request.user.is_authenticated and request.user.is_teacher:
            return render(request, 'mycourses/teacher/home.html')
        elif request.user.is_authenticated and request.user.is_student:
            return render(request, 'mycourses/student/home.html')
        else:
            return render(request, 'mycourses/bases/home.html', self.context)


class AccountView(View):
    def get(self, request):
        print(request.user)
        if request.user.is_authenticated and request.user.is_teacher:
            return render(request, 'mycourses/teacher/home.html', {"user": request.user})
        elif request.user.is_authenticated and request.user.is_student:
            return render(request, 'mycourses/student/home.html', {"user": request.user})
        else:
            return redirect('home')


class AccountCreate(View):

    def post(self, request):
        form = SubjectForm(request.POST)
        post = form.save()
        # post.author = request.user
        # post.published_date = timezone.now()
        post.save()
        return redirect('view_subjects', subjects_id=post.pk)

    def get(self, request):
        form = SubjectForm()
        return render(request, 'mycourses/teacher_edit.html', {'form': form})


class SubjectView(View):
    def get(self, request, subjects_id):
        # news_item = News.objects.get(pk=news_id)
        news_item = get_object_or_404(Subject, pk=subjects_id)
        return render(request, 'mycourses/view_course.html', {"news_item": news_item})




