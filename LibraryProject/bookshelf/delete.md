# Delete
b = Book.objects.get(title="Nineteen Eighty-Four")
b.delete()
# Expected output:
# (1, {'bookshelf.Book': 1})
Book.objects.all()
# Expected output:
# <QuerySet []>
