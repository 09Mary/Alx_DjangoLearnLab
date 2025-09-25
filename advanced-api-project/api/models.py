from django.db import models

# Author model stores writer's name
class Author(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name}"

# Book model links each book to an author via ForeignKey
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
