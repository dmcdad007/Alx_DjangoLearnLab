from django.db import models

# Author model represents a single book author.
# It currently stores only a name field, but it can be expanded later
# (e.g., biography, birthdate, etc.)
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model represents individual books.
# Each book is linked to an Author using a ForeignKey, forming a
# one-to-many relationship: one author can have many books.
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    
    # ForeignKey creates a relationship so that each Book belongs to an Author.
    # related_name='books' allows reverse access: author.books.all()
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
