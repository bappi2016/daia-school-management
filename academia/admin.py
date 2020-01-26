from django.contrib import admin
from .models import Teacher,Classes

# Register your models here.


@admin.register(Classes)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['class_name','class_duration','available_seats','tution_fee']

    search_fields = ['class_instructor']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['teachers_name','teachers_speciality']
