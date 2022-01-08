import django
from django.urls import path

from . import views
from .views import *

urlpatterns = [
     path('mycourses/done', MyCoursesDone.as_view(), name='done'),
     path('mycourses', MyCoursesCreate.as_view(), name='create'),
     path('mycourses/<int:pk>', MyCoursesRetrieveUpdateDestroy.as_view(), name='create'),

]
