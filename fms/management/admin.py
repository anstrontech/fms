from django.contrib import admin
from management.models import User,Course,Faculty_subject,Subject,Course_subject,Question,Feedback_reply
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("enrollNo","fullName","emailID","password","contact","role","course","semester","created_at")
    search_fields = ("enrollNo","fullName","emailID","contact","course")
    ordering = ('id',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("courseID","courseName",)
    search_fields = ("courseName",)
    ordering = ('id',)

@admin.register(Faculty_subject)
class Faculty_subjectAdmin(admin.ModelAdmin):
    list_display = ("faculty","course","semester","subjectName",)
    search_fields = ("subjectName","faculty","course")
    ordering = ('id',)

@admin.register(Course_subject)
class Course_subjectAdmin(admin.ModelAdmin):
    list_display = ("course","semester","subjectName",)
    search_fields = ("subjectName","course")
    ordering = ('id',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("subjectID","subjectName",)
    search_fields = ("subjectName",)
    ordering = ('id',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("questionid","question","created_at")
    search_fields = ("question",)
    ordering = ('id',)

@admin.register(Feedback_reply)
class Feedback_replyAdmin(admin.ModelAdmin):
    list_display = ("studentid","facultyid","subjectid","courseid","rating","created_at")
    search_fields = ("studentid","facultyid","subjectid","courseid","rating")
    ordering = ('id',)