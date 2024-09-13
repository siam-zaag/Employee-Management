from django.contrib import admin
from .models import Employee
# Register your models here.

@admin.register(Employee)
class Employee(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'mobile')
    search_fields = ('first_name','last_name')