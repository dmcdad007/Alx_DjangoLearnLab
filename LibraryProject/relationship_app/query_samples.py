import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1) Query all books by a specific author
author = Author.objects.filter(name='Jane Doe').first()
if author:
    books_by_author = Book.objects.filter(author=author)
    print("Books by", author.name, ":", [b.title for b in books_by_author])

# 2) List all books in a library
library = Library.objects.filter(name='Central Library').first()
if library:
    library_books = library.books.all()
    print("Books in", library.name, ":", [b.title for b in library_books])

# 3) Retrieve the librarian for a library
if library:
    # via reverse OneToOne accessor
    try:
        librarian = library.librarian
        print("Librarian for", library.name, ":", librarian.name)
    except Librarian.DoesNotExist:
        print("No librarian assigned to", library.name)