from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import re
from management.models import User, Course, Subject, Faculty_subject, Course_subject, Question, Feedback_reply

from management.functions import setTosession, roleType, semester, fetchAllCourse, fetchAllSubject, valiDateUser,enroll
from django.core import serializers
import math


# Login View And Login Controller


def login(request):
    enrollno = ""
    password = ""
    if (request.POST):
        enrollno = request.POST['username']
        password = request.POST['password']
        if (enrollno.strip() != "" and password != ""):
            user = User.objects.filter(
                enrollNo=enrollno.strip(), password=password)
            userstaus = {}
            for u_s in user:
                userstaus = u_s.__dict__

            if(not bool(userstaus)):
                return render(request, "login.html", {"message": "Invalid User"})
            else:
                setTosession(request, userstaus)
                return redirect("/")
        else:
            return render(request, "login.html", {"message": "Required Feild Is Empty"})

    if ('session' in request.session):
        # Mange Dashboard Data Accordingly ('a','f','s')

        return render(request, "dashboard.html", dashboardData(role=request.session['session']['role'], course=request.session['session']['course'], id_=request.session['session']['userid']))
    else:
        return render(request, "login.html", {'title': 'Login'})

# View Add User


def dashboardData(**kwargs):

    if(kwargs['role'] == "a"):
        count = {}
        courses_ = Course.objects.all()
        for course in courses_:
            cr_dit = course.__dict__
            count[cr_dit['courseName']] = User.objects.filter(course=cr_dit['courseID'], role="s").count()

        
        return {"count" : count}

    elif(kwargs['role'] == "f"):
        pattern = "[0-9]"
        count = {}
        course_add_student = kwargs['course'].split(",")
        courses = {}
        for i_i in course_add_student:
            count[re.sub(pattern, "", i_i)] = User.objects.filter(
                course=i_i, role="s").count()

        faculty_info = Feedback_reply.objects.filter(facultyid=kwargs['id_'])

        faculty__info = []
        for faculty in faculty_info:
            info_dict = faculty.__dict__

            faculty_name = User.objects.filter(
                userid=info_dict['facultyid'])[0].__dict__
            info_dict['facultyid'] = faculty_name['fullName']

            subject_name = Subject.objects.filter(
                subjectID=info_dict['subjectid'])[0].__dict__
            info_dict['subjectid_'] = subject_name['subjectName']

            course_name = Course.objects.filter(
                courseID=info_dict['courseid'])[0].__dict__
            info_dict['courseid'] = course_name['courseName']

            faculty__info.append(info_dict)

        feedback = {}
        counter  = {}
        for operation in faculty__info:
            counter[operation['subjectid_']] = Feedback_reply.objects.filter(subjectid=operation['subjectid']).count()
            try:
                if (operation['courseid'] not in feedback):
                    feedback[operation['courseid']] = {}
                if (operation['subjectid_'] not in feedback[operation['courseid']]):
                    feedback[operation['courseid']][operation['subjectid_']] = {}
                
                if ("rating" not in feedback[operation['courseid']][operation['subjectid_']]):
                    feedback[operation['courseid']][operation['subjectid_']]['rating'] = 0

                feedback[operation['courseid']][operation['subjectid_']]['rating']  += float(operation['rating'])
                feedback[operation['courseid']][operation['subjectid_']]['semester']  = operation['semester']
                feedback[operation['courseid']][operation['subjectid_']]['counter'] = counter[operation['subjectid_']]
            except:
                pass  

        for course,subjectdict in feedback.items():
            for subject,data in subjectdict.items():
                feedback[course][subject]['rating'] = math.floor((data['rating']/data['counter'])*100)

        return {"count": count,"feedback" : feedback}
    
    return {}

def adduser(request):

    enrollNo = ""
    full_name = ""
    email = ""
    contact = ""
    course = ""
    semester_ = ""
    role = ""

    if(request.POST):
        enrollNo = request.POST['enrollno'] if request.POST['enrollno'] != "" else enroll()
        full_name = request.POST['full_nmae']
        email = request.POST['email']
        contact = request.POST['phone']
        course = ",".join(request.POST.getlist('course'))
        semester_ = request.POST['semester']
        role = request.POST['role']

        User.objects.create(enrollNo=enrollNo, fullName=full_name, emailID=email,
                            contact=contact, course=course, semester=semester_, role=role, parentid=request.session['session']['userid'])

        return redirect("/adduser/")

    if ('session' in request.session):
        # Permission
        if (valiDateUser(request.session['session']['role'], ['a', 'f'])):
            if (request.session['session']['role'] == "a"):
                courses = dict(fetchAllCourse(Course))
            elif (request.session['session']['role'] == "f"):
                pattern = "[0-9]"
                course_add_student = request.session['session']['course'].split(
                    ",")
                courses = {}
                for i_i in course_add_student:
                    courses[i_i] = re.sub(pattern, "", i_i)

            role = dict(roleType())
            semesters = dict(semester())
            data = {
                'courses': courses,
                'role': role,
                'semesters': semesters
            }
            return render(request, "adduser.html", data)
        else:
            return redirect("/")

    else:
        return render(request, "login.html", {'title': 'Login'})

# View Users


def viewuser(request):
    if ('session' in request.session):
        return render(request, "viewuser.html", {'users': [u_s.__dict__ for u_s in User.objects.exclude(userid=request.session['session']['userid'])]})
    else:
        return render(request, "login.html", {'title': 'Login'})

# View / Add Course


def viewaddcourse(request):
    if(request.POST):
        Course.objects.create(courseName=request.POST['coursenaem'])
        return redirect("/course/")
    if ('session' in request.session):
        return render(request, "addviewcourse.html", {'course': [c_s.__dict__ for c_s in Course.objects.all()]})
    else:
        return render(request, "login.html", {'title': 'Login'})

# View / Add Subject


def addviewsubject(request):
    if(request.POST):
        Subject.objects.create(subjectName=request.POST['subjectnaem'])
        return redirect("/subject/")
    if ('session' in request.session):
        return render(request, "addviewsubject.html", {'subject': [s_s.__dict__ for s_s in Subject.objects.all()]})
    else:
        return render(request, "login.html", {'title': 'Login'})

# ALLOCATING FACULTY WITH SUBJECT


def viewaddfacultysubject(request):

    if(request.POST):
        Faculty_subject.objects.create(faculty=",".join(request.POST.getlist(
            'faculty')), course=request.POST['course'], semester=request.POST['semester'], subjectName=",".join(request.POST.getlist('subjects')))
        return redirect("/faculty_subject/")

    if ('session' in request.session):
        courses = [c_s.__dict__ for c_s in Course.objects.all()]
        faculty = [u_r.__dict__ for u_r in User.objects.filter(role='f')]
        semesters = dict(semester())
        subjects = [s_s.__dict__ for s_s in Subject.objects.all()]
        faculty_subject = [
            f_s.__dict__ for f_s in Faculty_subject.objects.all()]

        return render(request, "faculty_subject.html", {'faculty': faculty, 'course': courses, 'semester': semesters, 'subject': subjects, 'faculty_subject': faculty_subject})
    else:
        return render(request, "login.html", {'title': 'Login'})


def viewaddcoursesubject(request):
    if(request.POST):
        Course_subject.objects.create(course=request.POST['course'], semester=request.POST['semester'], subjectName=",".join(
            request.POST.getlist('subjects')))
        return redirect("/course_subject/")

    if ('session' in request.session):
        courses = [c_s.__dict__ for c_s in Course.objects.all()]
        faculty = [u_r.__dict__ for u_r in User.objects.filter(role='f')]
        semesters = dict(semester())
        subjects = [s_s.__dict__ for s_s in Subject.objects.all()]
        faculty_subject = [
            f_s.__dict__ for f_s in Course_subject.objects.all()]

        return render(request, "course_subject.html", {'course': courses, 'semester': semesters, 'subject': subjects, 'faculty_subject': faculty_subject})
    else:
        return render(request, "login.html", {'title': 'Login'})


def viewaddfeedbackqus(request):
    if(request.POST):
        qs = Question.objects.filter(question=request.POST['quesiton'])
        if (len(qs) > 0):
            feedabckqus = [
                f_s.__dict__ for f_s in Question.objects.all()]
            return render(request, "feedback_qus.html", {"message": "Duplicate Entry", 'feedabckqus': feedabckqus})
        Question.objects.create(question=request.POST['quesiton'])
        return redirect("/feedback_qus/")

    if ('session' in request.session):
        feedabckqus = [
            f_s.__dict__ for f_s in Question.objects.all()]
        return render(request, "feedback_qus.html", {'feedabckqus': feedabckqus})
    else:
        return render(request, "login.html", {'title': 'Login'})


def give_feedback(request):

    if(request.POST):
        sutedentid = request.POST['studentid']
        courseid = request.POST['courseid']
        semester = request.POST['semester']
        faculty = request.POST['faculty']
        subjects = request.POST['subjects']

        isGiven = Feedback_reply.objects.filter(studentid=sutedentid, courseid=courseid, semester=semester, facultyid=faculty, subjectid=subjects,rating="")


        if (isGiven.count() <= 0):
            Feedback_reply.objects.create(
            studentid=sutedentid, courseid=courseid, semester=semester, facultyid=faculty, subjectid=subjects)

            id_ = Feedback_reply.objects.latest('id')

            id_ = id_.__dict__['qformid']
            return redirect(f"/feedback/?setid={id_}&u={faculty}&s={subjects}")

        id_ = isGiven[0].__dict__['qformid']
        return redirect(f"/feedback/?setid={id_}&u={faculty}&s={subjects}")
        

    if ('session' in request.session):
        # Permission
        if (valiDateUser(request.session['session']['role'], ['s'])):

            faculty = [u_r.__dict__ for u_r in User.objects.filter(
                role='f', course__contains=request.session['session']['course'])]
            data = {
                'faculty': faculty
            }
            return render(request, "give_feedback.html", data)
        else:
            return redirect("/")
    else:
        return render(request, "login.html", {'title': 'Login'})


def feedback(request):
    if(request.POST):
        rating = []
        for r_p in request.POST:
            if(r_p != "csrfmiddlewaretoken"):
                rating.append(int(request.POST[r_p]))

        total = len(Question.objects.all())*5
        rate = sum(rating)/total
        setid = request.GET['setid']

        Feedback_reply.objects.filter(qformid=setid).update(rating=rate)
        return redirect("/give_feedback/")

    if ('session' in request.session):

        # Permission
        if (valiDateUser(request.session['session']['role'], ['s'])):

            setid = request.GET['setid']
            f = request.GET['u']
            s = request.GET['s']
            usr = User.objects.filter(userid=f)
            sub = Subject.objects.filter(subjectID=s)
            usr = usr[0].__dict__
            sub = sub[0].__dict__
            username = usr['fullName']
            subname = sub['subjectName']

            question = [u_r.__dict__ for u_r in Question.objects.all()]

            return render(request, "feedback.html", {'name': username, 'subject': subname, 'question': question})

        else:
            return redirect("/")
    else:
        return render(request, "login.html", {'title': 'Login'})


def get_faculty_subject(request):
    facultyid = request.POST['faculty']
    course = request.POST['course']
    semester_ = request.POST['semester']

    try:
        subjectsid = Faculty_subject.objects.filter(
            faculty=facultyid, course=course, semester=semester_)
        serialized_subject = serializers.serialize('python', subjectsid)
        subjectsid = serialized_subject[0]['fields']['subjectName'].split(',')

        reponse = []

        for sub_id in subjectsid:
            sub__serialize = Subject.objects.filter(subjectID=sub_id)
            serialized_subjects = serializers.serialize(
                'python', sub__serialize)
            reponse.append(serialized_subjects[0]['fields'])

        return JsonResponse(reponse, safe=False)
    except:
        pass

# LOGOUT SESSIOn


def logout(request):
    request.session.flush()
    request.session.clear_expired()
    return redirect('/')