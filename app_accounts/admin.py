from django.contrib import admin
from app_accounts.models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(Avatar)

class Accountinline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = "Perfiles"


class CustomizedUserAdmin (UserAdmin):
    inlines = (Accountinline, )

admin.site.unregister (User)
admin.site.register (User, CustomizedUserAdmin)
