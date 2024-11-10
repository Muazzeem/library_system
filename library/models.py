from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    publication_date = models.DateField()
    genre = models.CharField(max_length=100)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title

