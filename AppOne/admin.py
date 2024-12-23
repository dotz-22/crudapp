from django.contrib import admin
from .models import BooksModel

# Register your models here.
class AdminModel(admin.ModelAdmin):
    list_display = ("id", "book_title", "book_author", "publishing_date", "description" )
    search_fields = ("book_title", "book_author", "publishing_date", "description" )

admin.site.register(BooksModel, AdminModel)