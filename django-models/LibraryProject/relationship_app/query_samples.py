from relationship_app.models import Author, Book, Library, Librarian

# 1) Query all books by a specific author
author = Author.objects.filter(name='Jane Doe').first()
if author:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print("Books by", author.name, ":", [b.title for b in books_by_author])


# 2️⃣ List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

# 3️⃣ Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian  # OneToOneField allows direct access
    return librarian


# Example usage (for testing in Django shell):
if __name__ == "__main__":
    # Make sure to run: python manage.py shell < relationship_app/query_samples.py
    print("Books by 'J.K. Rowling':", list(get_books_by_author("J.K. Rowling")))
    print("Books in 'Central Library':", list(get_books_in_library("Central Library")))
    print("Librarian for 'Central Library':", get_librarian_for_library("Central Library"))


