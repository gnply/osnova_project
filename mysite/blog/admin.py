from django.contrib import admin

from .models import *

class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name', 'middle_name', 'project', 'active']
    list_display = ('time_created', 'last_name', 'first_name', 'middle_name', 'project', 'role_in_project' ,'personal_score', 'score','init', 'active')
    list_editable = ('active', 'score')
    ordering = ('active', '-score')

class ScoreAdmin(admin.ModelAdmin):
    search_fields = ['project_name']
    list_display = ('project_name', 'fio', 'score', 'project_score', 'type_project')



admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Score, ScoreAdmin)