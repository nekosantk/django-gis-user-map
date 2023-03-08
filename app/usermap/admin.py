from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UpdateUserForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UpdateUserForm
    model = CustomUser
    list_display = ("email", "location", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = ((None, {"fields": ("email", "password")}), ("Permissions", {
        "fields": ("is_staff", "is_active", "groups", "user_permissions")}), )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions", "location"
            )}
         ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
