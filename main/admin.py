from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'is_active']
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_('Extra'), {'fields': ('type', 'number', 'image')}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
admin.site.register(Client)
admin.site.register(Room)
admin.site.register(Maxsulot)
admin.site.register(Order)
admin.site.register(Meal)
admin.site.register(OrderItem)
