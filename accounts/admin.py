from django.contrib import admin
from .models import Contact
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Department, Employee


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'submitted_at')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin, admin.ModelAdmin):   
    list_display = ('name', 'employee_id', 'department',)
    search_fields = ('name', 'employee_id', 'department')
    list_filter = ('department',)

