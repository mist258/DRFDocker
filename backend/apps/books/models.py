from django.db import models

class Book(models.Model):
    class Meta:
        db_table = 'books'

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)