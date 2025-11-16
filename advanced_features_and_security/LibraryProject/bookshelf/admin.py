from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    list_filter = ("publication_year", "author")
    search_fields = ("title", "author")
    ordering = ("-publication_year", "title")
    list_per_page = 25

# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    """Admin interface for CustomUser."""

    # Fields displayed in the list view
    list_display = ("email", "first_name", "last_name", "date_of_birth", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "date_of_birth")
    search_fields = ("email", "first_name", "last_name")

    # Layout of the change form
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    # Fields shown when adding a new user
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "date_of_birth", "profile_photo"),
        }),
    )

    ordering = ("email",)
    filter_horizontal = ("groups", "user_permissions",)
