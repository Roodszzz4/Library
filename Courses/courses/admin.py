from django.contrib import admin
from .models import Course, Teacher, Subject


#admin.site.register(Course)
admin.site.register(Teacher)
#admin.site.register(Subject)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'course_display')
    filter_horizontal = ('course',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher')