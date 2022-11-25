from django.contrib import admin

from .models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    fields = ('name','email','username','phone')

admin.site.register(Student, StudentAdmin)
admin.site.register(UserRole)
