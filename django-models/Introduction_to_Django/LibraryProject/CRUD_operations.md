# Create
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Expected output:
# <Book: 1984 by George Orwell (1949)>
# book.id -> 1  # actual id may differ

# Retrieve
from bookshelf.models import Book
books = Book.objects.all()
# Expected output:
# <QuerySet [<Book: 1984 by George Orwell (1949)>]>
b = Book.objects.get(title="1984")
# Expected output for fields:
# b.title -> '1984'
# b.author -> 'George Orwell'
# b.publication_year -> 1949

# Update
b = Book.objects.get(title="1984")
b.title = "Nineteen Eighty-Four"
b.save()
b.refresh_from_db()
# Expected output:
# b.title -> 'Nineteen Eighty-Four'

# Delete
b = Book.objects.get(title="Nineteen Eighty-Four")
b.delete()
# Expected output:
# (1, {'bookshelf.Book': 1})
Book.objects.all()
# Expected output:
# <QuerySet []>
