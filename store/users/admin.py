from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from products.admin import BasketAdminInline

from users.models import User

UserAdmin.fieldsets += (
    ('Extra Fields', {'fields': ('image',)}),
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdminInline, )
