from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from . import models
# Register your models here.


class UserAdmin(BaseAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    #  you need to add your custom fields to fieldsets (for fields to be used in editing users) and
    #  to add_fieldsets (for fields to be used when creating a user).
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password',)}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'name', 'password'),
        }),
    )

admin.site.register(models.User, UserAdmin)