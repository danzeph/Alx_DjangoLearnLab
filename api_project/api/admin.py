from django.contrib import admin
from api.models import Book

class BookAdmin(admin.ModelAdmin):
    list_filter = ['title', 'published_date']
    search_fields = ['author', 'title']
    list_display = ['title', 'author', 'published_date','created_at']

admin.site.register(Book, BookAdmin)
