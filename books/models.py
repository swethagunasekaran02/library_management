# books/models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="books")
    isbn = models.CharField(max_length=13, unique=True)
    total_copies = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)


    def __str__(self):
        return f"{self.title} by {self.author.name if self.author else 'Unknown'}"

