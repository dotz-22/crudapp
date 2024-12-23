from django.db import models

# Create your models here.



class BooksModel(models.Model):
    book_title = models.CharField(max_length=250)
    book_author = models.CharField(max_length=200)
    publishing_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)