from django.contrib import admin
from izeni.django.accounts.admin import EmailUserAdmin
from .models import EmailUser
class UserAdmin(EmailUserAdmin):
    pass
admin.site.register(EmailUser, EmailUserAdmin)
