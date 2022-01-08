from django.urls import path

from mycourses.views.personalteacher import CreateCourse, ShowCourses, ShowCourse, CreateLesson, CreateStudent, \
    ShowLesson, UpdateLesson, ShowStudent, UpdateStudent
from mycourses.views.views import *
from mycourses.views.signup import *



urlpatterns = [
    # path('about/', MorningGreetingView.as_view(greeting='Privet'), name='about'),
    path('courses/', HomeCourses.as_view(), name='courses'),


    # # path('teachers/<int:category_id>/', TeacherByCategory.as_view(), name='teachers'),
    # # path('teachers/', PublisherList.as_view(), name='teachers'),
    path('courses/<int:subjects_id>/', SubjectView.as_view(), name='view_subjects'),
    path('category/<int:category_id>/', CourseByCategory.as_view(), name='courses'),



    # bases
    path('', HomeView.as_view(), name='home'),
    path('about/', HomeView.as_view(), name='about'),
    # path('', HomeView.as_view(), name='home'),

    # signup
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('account/teacher_edit.html', AccountCreate.as_view(), name='course_edit'),
    path('login/', UserLogin.as_view(), name='login'),
    path('update/', Update.as_view(), name='update'),


    # signup
    # path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    # path('signup/student/', Register.as_view(), name='student_signup'),
    # path('accounts/signup/teacher/', teachersignup.TeacherSignUpView.as_view(), name='teacher_signup'),
    # student
    path('account/', AccountView.as_view(), name='homebystudent'),


    # teacher
    path('account/', AccountView.as_view(), name='homebyteacher'),
    path('create/', CreateCourse.as_view(), name='create_course'),
    path('show/', ShowCourses.as_view(), name='show_courses'),
    path('show/<int:course_id>/', ShowCourse.as_view(), name='show_course'),
    path('show/<int:course_id>/create_lesson', CreateLesson.as_view(), name='create_lesson'),
    path('show/<int:course_id>/lesson/<int:lesson_id>', ShowLesson.as_view(), name='show_lesson'),
    path('show/<int:course_id>/lesson/<int:lesson_id>/update', UpdateLesson.as_view(), name='update_lesson'),
    path('show/<int:course_id>/create_student', CreateStudent.as_view(), name='create_student'),
    path('show/<int:course_id>/student/<int:student_id>', ShowStudent.as_view(), name='show_student'),
    path('show/<int:course_id>/student/<int:student_id>/update', UpdateStudent.as_view(), name='update_student'),
    # path('teachers/<int:teachers_id>/', TeacherByCategory.as_view(), name='teachers'),

    path('account/teacher_edit.html', AccountCreate.as_view(), name='course_edit'),
]
