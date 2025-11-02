# Update
b = Book.objects.get(title="1984")
b.title = "Nineteen Eighty-Four"
b.save()
b.refresh_from_db()
# Expected output:
# b.title -> 'Nineteen Eighty-Four'
