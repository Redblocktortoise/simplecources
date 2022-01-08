from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import *


class MyCoursesDone(generics.ListAPIView):
    serializer_class = MyCoursesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Subject.objects.all()


class MyCoursesCreate(generics.ListCreateAPIView):
    serializer_class = MyCoursesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Subject.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class MyCoursesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MyCoursesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Subject.objects.all()
