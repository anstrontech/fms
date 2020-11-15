import string
import random
from django.db import connection

def RandomID(length = 7):
    uniqueID = str(random.random())
    return uniqueID[2:length]

def enroll():
    return RandomID(12)
    
def semester():
    return [(str(x), str(x)) for x in range(1,7)]

def userid():
    return "USER"+RandomID()

def roleType():
    return [
        ('a',"Admin"),
        ('f',"Faculty"),
        ('s',"Student"),
    ]

def setTosession(request,data):
    request.session['session'] = {}
    for key,value in data.items():
        if(key != "_state"):
            request.session['session'][key] = str(value)

    return request.session['session']

def fetchAllCourse(course):
    return [(courses.courseID,str(courses.courseName)) for courses in course.objects.all()]

def fetchAllQuestion(quesiton):
   return [(str(f_s.questionid),str(f_s.question)) for f_s in quesiton.objects.all()]

def fetchAllFaculty(users):
    return [(str(user.userid),str(user.fullName)) for user in users.objects.filter(role='f')]

def fetchAllStudent(users):
    return [(str(user.userid),str(user.fullName)) for user in users.objects.filter(role='s')]

def fetchAllSubject(subject):
    return [(str(sub.subjectID),str(sub.subjectName)) for sub in subject.objects.all()]

def valiDateUser(role,permission):
    if(role in permission):
        return True
    else:
        return False
    