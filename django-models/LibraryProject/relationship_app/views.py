from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library
from django.views.generic import DetailView


# ---------- Function-based view ----------
def list_books(request):
    """Display a list of all books and their authors."""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

