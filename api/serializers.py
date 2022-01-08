from rest_framework import serializers

from mycourses.models import *


class MyCoursesSerializer (serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ['id', 'name', 'content', 'photo']



