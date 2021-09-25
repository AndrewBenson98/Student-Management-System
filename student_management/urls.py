from django.urls import path
from .views import StudentListView, StudentCreateView, StudentDetailView, StudentUpdateView, StudentDeleteView
from .views import CourseListView , CourseDetailView ,CourseCreateView, CourseUpdateView, CourseDeleteView
from .views import EnrollCourseView, UpdateGradeView, UnenrollView
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    #Student Urls
    path('', StudentListView.as_view(), name='student-list'),
    path('student/create/', StudentCreateView.as_view(), name='student-create'),
    path('student/<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    
    #Course Urls
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/create/', CourseCreateView.as_view(), name='course-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/<int:pk>/update/', CourseUpdateView.as_view(), name='course-update'),
    path('courses/<int:pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),
    
    #Enrollment Urls
    path('course_enrollment/', EnrollCourseView.as_view(), name='student-enrollment'),
    path('course/grade/update/<int:pk>/', UpdateGradeView.as_view(), name='student-grade-update'),
    path('course_unenrollment/<int:pk>/', UnenrollView.as_view(), name='student-unenrollment'),
    
    
    #Login urls
    path('login/', auth_views.LoginView.as_view(template_name='student_management/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='student_management/logout.html'), name='logout'),
    
]
