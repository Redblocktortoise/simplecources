from django.contrib import admin

from .models import *


@admin.register(Lesson, Category, Subject, Student, User, Teacher, Team)
class PersonAdmin(admin.ModelAdmin):
    pass
