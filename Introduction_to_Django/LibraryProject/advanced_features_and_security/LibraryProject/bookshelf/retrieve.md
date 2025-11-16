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
