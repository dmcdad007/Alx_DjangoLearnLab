# Open Django shell:
# $ python manage.py shell

from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Expected output (example representation returned by create):
# <Book: 1984 by George Orwell (1949)>

# Or when printing:
print(book)
# Expected printed output:
# 1984 by George Orwell (1949)
