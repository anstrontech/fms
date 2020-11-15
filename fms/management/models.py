from django.db import models
from management.functions import semester, roleType,fetchAllCourse,fetchAllFaculty,fetchAllSubject,fetchAllStudent,fetchAllQuestion

# Create your models here.
class Course(models.Model):
    courseID = models.CharField(
        max_length=100, blank=True, editable=False, unique=True)
    courseName = models.CharField(max_length=100, unique=True)

class Subject(models.Model):
    subjectID = models.CharField(
        max_length=100, blank=True, editable=False, unique=True)
    subjectName = models.CharField(max_length=100, unique=True)

class User(models.Model):
    userid      = models.CharField(max_length=10, blank=True, editable=False, unique=True)
    enrollNo    = models.CharField(max_length=100, unique=True,blank=True)
    fullName    = models.CharField(max_length=100)
    emailID     = models.CharField(max_length=100, unique=True)
    password    = models.CharField(max_length=100, blank=True, editable=False)
    contact     = models.CharField(max_length=100, unique=True)
    course      = models.CharField(max_length=100,choices=fetchAllCourse(Course),blank=True)
    semester    = models.CharField(max_length=100,choices=semester(),blank=True)
    role        = models.CharField(max_length=100, choices=roleType(), default='s')
    college     = models.CharField(max_length=100, default="CPICA",editable=False)
    parentid    = models.CharField(max_length=10, blank=True, editable=False)
    created_at  = models.DateField(auto_now_add=True, blank=True)
    updated_at  = models.DateField(auto_now_add=True, blank=True)

class Faculty_subject(models.Model):
    faculty     = models.CharField(max_length=100,choices=fetchAllFaculty(User),default=None)
    course      = models.CharField(max_length=100,choices=fetchAllCourse(Course),default=None)
    semester    = models.CharField(max_length=100,choices=semester(), default=1)
    subjectName = models.CharField(max_length=100,choices=fetchAllSubject(Subject),default=None)

class Course_subject(models.Model):
    course      = models.CharField(max_length=100,choices=fetchAllCourse(Course),default=None)
    semester    = models.CharField(max_length=100,choices=semester(), default=1)
    subjectName = models.CharField(max_length=100,choices=fetchAllSubject(Subject),default=None)

class Question(models.Model):
    questionid    = models.CharField(max_length=10, blank=True, editable=False, unique=True)
    question    = models.CharField(max_length=200,default=None,null=False,unique=True)
    created_at  = models.DateField(auto_now_add=True, blank=True)
    updated_at  = models.DateField(auto_now_add=True, blank=True)

class Feedback_reply(models.Model):
    qformid     = models.CharField(max_length=10, blank=True, editable=False, unique=True)
    facultyid   = models.CharField(max_length=10,choices=fetchAllFaculty(User), blank=False)
    studentid   = models.CharField(max_length=10, choices=fetchAllStudent(User),blank=False)
    subjectid   = models.CharField(max_length=10,choices=fetchAllSubject(Subject) , blank=False)
    courseid    = models.CharField(max_length=10,choices=fetchAllCourse(Course), blank=False)
    semester    = models.CharField(max_length=10,choices=semester(), blank=False)
    rating      = models.CharField(max_length=10, blank=True)
    created_at  = models.DateField(auto_now_add=True, blank=True)
    updated_at  = models.DateField(auto_now_add=True, blank=True)