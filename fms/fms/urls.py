"""fms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from management import views

urlpatterns = [
    path('',views.login,name='login'),
    path('login/',views.login,name='loginctrl'),
    path('logout/',views.logout,name='logout'),
    path('adduser/',views.adduser,name='adduser'),
    path('viewuser/',views.viewuser,name='viewuser'),
    path('course/',views.viewaddcourse,name='viewaddcourse'),
    path('subject/',views.addviewsubject,name='viewaddsubject'),
    path('faculty_subject/',views.viewaddfacultysubject,name='faculty_subject'),
    path('course_subject/',views.viewaddcoursesubject,name='course_subject'),
    path('feedback_qus/',views.viewaddfeedbackqus,name='feedback_qus'),
    path('give_feedback/',views.give_feedback,name='give_feedback'),
    path('get_faculty_subject/',views.get_faculty_subject,name='get_faculty_subject'),
    path('feedback/',views.feedback,name='feedback'),
    path('admin/', admin.site.urls),
]
