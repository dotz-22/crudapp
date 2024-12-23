from django.contrib import admin
from .models import AuthorsModel

# Register your models here.

class AdminModel(admin.ModelAdmin):
    list_display = ("id", "name", "bio", "date_of_birth")
    search_fields = ("name", "bio", "date_of_birth")

admin.site.register(AuthorsModel, AdminModel)