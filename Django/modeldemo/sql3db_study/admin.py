from django.contrib import admin
from sql3db_study.models import employee

# Register your models here.
class employeeAdmin(admin.ModelAdmin):
    list_display = ('eno', 'ename', 'esal', 'eaddr')
admin.site.register(employee, employeeAdmin)

