from django.db.models.fields import DecimalField
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Student, Course,EnrolledCourse
# Create your views here.


#Student Views ----------------------------------------------------------------

class StudentListView(ListView):
    template_name='student_management/student-list.html'
    model = Student
    context_object_name = 'students'
    paginate_by =5
    ordering = ['name']
    
    
class StudentCreateView(LoginRequiredMixin,CreateView):
    model = Student
    template_name = 'student_management/student-create.html'
    fields = ['studentID', 'name', 'email', 'phoneNumber']
    
    
class StudentUpdateView(LoginRequiredMixin,UpdateView):
    model = Student
    template_name = 'student_management/student-create.html'
    fields = ['studentID', 'name', 'email', 'phoneNumber', 'gpa']
    
    

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_management/student-detail.html'
    context_object_name ='student'
    
    #Get Context: All the courses the student is enrolled in
    def get_context_data(self, **kwargs):
        student = get_object_or_404(Student, pk=self.kwargs.get('pk'))
        enrolled_courses = EnrolledCourse.objects.filter(student=student).order_by('course')
        context = super().get_context_data(**kwargs)
        context['enrolled_courses'] = enrolled_courses
        return context

class StudentDeleteView(LoginRequiredMixin,DeleteView):
    model = Student
    success_url = reverse_lazy('student-list')
    #template_name = 'student_management/student_confirm_delete.html'
    


#Course Views ----------------------------------------------------------------

class CourseListView(ListView):
    model = Course
    template_name ='student_management/course-list.html'
    context_object_name ='courses'
    paginate_by =5
    ordering = ['courseCode'] 
    

class CourseDetailView(DetailView):
    model = Course
    template_name = 'student_management/course-detail.html'
    context_object_name = 'course'
    
    def get_context_data(self, **kwargs):
        course = get_object_or_404(Course, pk=self.kwargs.get('pk'))
        enrolled_courses = EnrolledCourse.objects.filter(course=course).order_by('student')
        context = super().get_context_data(**kwargs)
        context['enrolled_courses'] = enrolled_courses
        return context
    

class CourseCreateView(LoginRequiredMixin,CreateView):
    model = Course
    template_name = 'student_management/course-create.html'
    fields = ['courseCode', 'courseName', 'description']


class CourseUpdateView(LoginRequiredMixin,UpdateView):
    model = Course
    template_name = 'student_management/course-create.html'
    fields = ['courseCode', 'courseName', 'description']


class CourseDeleteView(LoginRequiredMixin,DeleteView):
    model = Course
    success_url= reverse_lazy('course-list')
    template_name = 'student_management/course_confirm_delete.html'
    

#Enrollment Views ----------------------------------------------------------------

class EnrollCourseView(LoginRequiredMixin,CreateView):
    model = EnrolledCourse
    template_name = 'student_management/student-enrollment.html'
    fields = ['student', 'course']

class UpdateGradeView(LoginRequiredMixin,UpdateView):
    model = EnrolledCourse
    template_name = 'student_management/student-update-grade.html'
    context_object_name = 'enrolled_course'
    fields = ['grade']

class UnenrollView(LoginRequiredMixin,DeleteView):
    model = EnrolledCourse
    success_url = reverse_lazy('student-list')
    template_name= 'student_management/unenrollment_confirm_delete.html'
    