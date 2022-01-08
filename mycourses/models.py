from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.urls import reverse
from django.conf import settings


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return (self.user.first_name + " " + self.user.last_name)

class Team(models.Model):
    name = models.CharField(default="default name",  max_length=100)
    # start_at = models.DateTimeField(default="", null=True, blank=True)
    # end_till = models.DateTimeField(default="", null=True, blank=True)
    video_communication = models.CharField(max_length=100)
    log = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Student(models.Model):
    MARKS = (
        ('A+', 'Super'),
        ('A', 'Excellent'),
        ('B', 'Good'),
        ('C', 'Only fair'),
        ('D', 'Poor'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    mark = models.CharField(default='B', max_length=2, choices=MARKS)


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    exercise = models.TextField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


# class Lecturer(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()
#
#     def __str__(self):
#         return (self.first_name + " " + self.last_name)


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, default='SOME STRING',
                             verbose_name='Наименование категории')

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категории'


class Subject(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    content = models.TextField(blank=True, verbose_name='Контент')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Учитель')

    # def get_absolute_url(self):
    #      return reverse('view_subjects', kwargs={"subjects_id": self.pk})

    def __str__(self):
        return self.title

    def __str__(self):
        return self.name

# class Student(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()


# class StudentTeam(models.Model):
#     MARKS = (
#         ('A', 'Excellent'),
#         ('B', 'Good'),
#         ('C', 'Only fair'),
#         ('D', 'Poor'),
#     )
#
#     team = models.ForeignKey(Team, on_delete=models.CASCADE)
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     mark = models.CharField(default='B', max_length=1, choices=MARKS)
#
#     class Meta:
#         verbose_name_plural = "Ученик в группе"


# class Timetable(models.Model):
#     lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
#     team = models.ForeignKey(Team, on_delete=models.CASCADE)
#     start_at = models.DateTimeField()
#     end_till = models.DateTimeField()
#     video_communication = models.CharField(max_length=100)
#     log = models.CharField(max_length=100)
