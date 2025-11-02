from bookshelf.models import Book

# Fetch the book
b = Book.objects.filter(title="Nineteen Eighty-Four", author="George Orwell", publication_year=1949).first()

# Delete the book
if b:
    book.delete()
    # Expected return value from delete (tuple): (1, {'bookshelf.Book': 1})

# Confirm deletion: list all books
Book.objects.all()
# Expected output:
# <QuerySet []>
