from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from django_filters import rest_framework

class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer


# --------------------------------------------------------
# BOOK LIST VIEW
# --------------------------------------------------------
# Allows ANY user to:
#   - Retrieve a list of all books (GET)
#
# Also includes:
#   - Filtering (title, author, publication_year)
#   - Searching (title, author's name)
#   - Ordering (title, publication_year)
#
# This makes our list endpoint extremely flexible.
# --------------------------------------------------------
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Enable DRF filter backends
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    # Filtering parameters
    filterset_fields = ['title', 'author', 'publication_year']

    # Search parameters
    search_fields = ['title', 'author__name']

    # Ordering parameters
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering


# --------------------------------------------------------
# BOOK DETAIL VIEW
# --------------------------------------------------------
# Allows ANY user to:
#   - Retrieve a single book (GET)
# --------------------------------------------------------
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# --------------------------------------------------------
# BOOK CREATE VIEW
# --------------------------------------------------------
# Allows AUTHENTICATED users to:
#   - Create a new book (POST)
#
# Overrides perform_create to include custom logic if needed.
# Example: logging, custom validation hooks, etc.
# --------------------------------------------------------
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Custom logic can go here
        # Example: attach request.user as creator if needed
        serializer.save()


# --------------------------------------------------------
# BOOK UPDATE VIEW
# --------------------------------------------------------
# Allows AUTHENTICATED users to:
#   - Update an existing book (PUT, PATCH)
#
# Includes custom update hook for extended behavior.
# --------------------------------------------------------
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Custom logic (logging, validation, etc.)
        serializer.save()


# --------------------------------------------------------
# BOOK DELETE VIEW
# --------------------------------------------------------
# Allows AUTHENTICATED users to:
#   - Delete a book (DELETE)
# --------------------------------------------------------
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# ------------------------------------------------------
# LIST VIEW
# ------------------------------------------------------
# Allows unauthenticated users to view all books.
# Uses ListAPIView which provides GET method only.
# ------------------------------------------------------
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]



# ------------------------------------------------------
# DETAIL VIEW
# ------------------------------------------------------
# Allows anyone to retrieve a single book by ID.
# Uses RetrieveAPIView which provides GET only.
# ------------------------------------------------------
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]



# ------------------------------------------------------
# CREATE VIEW
# ------------------------------------------------------
# Allows authenticated users to create new Book entries.
# Uses CreateAPIView which provides POST only.
#
# Custom Behavior:
#   - perform_create(): where you can insert extra logic
#     such as logging, attaching request.user, etc.
# ------------------------------------------------------
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Custom hook during object creation.
        Insert additional validation or automatic field assignment here.
        """
        serializer.save()



# ------------------------------------------------------
# UPDATE VIEW
# ------------------------------------------------------
# Allows authenticated users to update existing books.
# Uses UpdateAPIView which provides PUT and PATCH.
#
# Custom Behavior:
#   - perform_update(): place for custom validation
# ------------------------------------------------------
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Custom hook for modifying update behavior.
        Useful for logging, custom validation, etc.
        """
        serializer.save()



# ------------------------------------------------------
# DELETE VIEW
# ------------------------------------------------------
# Allows authenticated users to delete books.
# Uses DestroyAPIView which provides DELETE only.
# ------------------------------------------------------
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

