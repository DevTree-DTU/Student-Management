from django.contrib import admin
from login.models import Student, Teacher, TimeTable, Assignment, Batch

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'DOB', 'admissionYear', 'branch')
    search_fields = ('name', 'email')
    list_filter = ('admissionYear','branch',)
    ordering = ('-name',)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email')
    search_fields = ('name', 'email')

admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(TimeTable)
admin.site.register(Assignment)
admin.site.register(Batch)
# Register your models here.
