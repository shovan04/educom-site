from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    fields = ('name','email','username','phone')

    list_display = ('name','username','send_mail')

    def send_mail(self, obj):
        return format_html(f'<a href="http://127.0.0.1:8000/send-mail/{obj.username}/{obj.SecKey}/" >Send Mail</a>')


admin.site.register(Student, StudentAdmin)
admin.site.register(UserRole)
