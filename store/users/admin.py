from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User

UserAdmin.fieldsets += (
    ('Extra Fields', {'fields': ('image',)}),
)

admin.site.register(User, UserAdmin)
