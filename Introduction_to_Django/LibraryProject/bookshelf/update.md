from bookshelf.models import Book

# Fetch the book
b = Book.objects.get(title="1984", author="George Orwell", publication_year=1949)

# Update the title
b.title = "Nineteen Eighty-Four"
b.save()

# Verify update
b = Book.objects.get(pk=b.pk)
b.title
# Expected output:
# "Nineteen Eighty-Four"

# Printing the object:
print(b)
# Expected printed output:
# Nineteen Eighty-Four by George Orwell (1949)

