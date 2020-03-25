from django.contrib import admin

# Register your models here.
from .models import Student, Course, Act, Timetable


class StudentAdmin(admin.ModelAdmin):
    info = ['student_id', 'real_name', 'grade', 'college', 'major', 'student_class']
    fieldsets = [
        (None,                   {'fields': ['user']}),
        ('Personal information', {'fields': info}),
    ]
    list_display = ('student_id', 'real_name', 'student_class')
    list_filter = ['grade', 'college', 'major', 'student_class']
    search_fields = ['student_id', 'real_name']


class CourseAdmin(admin.ModelAdmin):
    fields = ['title', 'week', 'day', 'time', 'student']
    list_display = ('title', 'student')


class ActAdmin(admin.ModelAdmin):
    fields = ['title', 'week', 'day', 'time', 'leader']
    list_display = ('title', 'leader')


class TimeTableAdmin(admin.ModelAdmin):
    fields = ['week', 'day', 'time', 'student_class', 'act']
    list_display = ('week', 'day', 'time', 'student_class', 'act')


# Re-register UserAdmin
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Act, ActAdmin)
admin.site.register(Timetable, TimeTableAdmin)
