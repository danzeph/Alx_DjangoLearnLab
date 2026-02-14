from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser

# @admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "date_of_birth", "is_staff")
    search_fields = ("username",)

    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {
            "fields":("date_of_birth", "profile_photo")
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
          ("Additional Info", {
            "fields": ("date_of_birth", "profile_photo")
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
    
# @admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('title', 'publication_year')

    search_fields = ('title', 'author', 'publication_year')

admin.site.register(Book, BookAdmin)

