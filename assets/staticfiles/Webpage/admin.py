from django.contrib import admin
from .models import Emp_details
# Register your models here.
@admin.register(Emp_details)
class EmpModelAdmin(admin.ModelAdmin):
    list_display = ['id','firstname','lastname','email','mobile','birth','gender','address','country','city','get_skills']

    def get_skills(self, obj):
            return ', '.join(str(skill) for skill in obj.skills.all())
    get_skills.short_description = 'Skills'