from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.urls import reverse
# Create your models here.

class Student(models.Model):
    studentID = models.CharField(max_length=9, unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    phoneNumber = models.CharField(max_length=15, blank=True)
    gpa = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    
    
    #Calculates the student's average grade as a percentage e.g 75.55%
    def get_average(self):
        enrolled_courses = EnrolledCourse.objects.filter(student=self)
        average = 0
        
        if len(enrolled_courses) == 0:
            return 0
        
        for enrolled_course in enrolled_courses:
            average+=enrolled_course.grade
        average=average/len(enrolled_courses)
        return average

    #Sets their gpa based off their enrolled courses
    def setGpa(self):
        averageGrade = self.get_average()
        #gpa = 4 * (averageGrade/100)
        #self.gpa= gpa
        self.gpa = averageGrade
        self.save()
        return 
    
    def get_absolute_url(self):
        return reverse('student-list')
    
    def __str__(self):
        return self.name
    

class Course(models.Model):
    courseCode = models.CharField(max_length=10, unique=True)
    courseName = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.courseName}"

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'pk':self.pk})
    

class EnrolledCourse(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    
    class Meta:
        unique_together = ('student', 'course')
    
    def __str__(self):
        return f"{self.student} -> {self.course}"
    
    #Whenever a student's grade is updated in any course, update their gpa
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.student.setGpa()
        
    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk':self.student.pk})

