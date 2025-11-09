from django.shortcuts import render
from django.contrib.auth import login
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.http import HttpResponse
from .models import Library
from django.views.generic.detail import DetailView


# ---------- Function-based view ----------
def list_books(request):
    """Display a list of all books and their authors."""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# ---------- User Registration ----------
def register_view(request):
    """Allow new users to register."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# ---------- User Login ----------
def login_view(request):
    """Allow existing users to log in."""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect('list_books')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid login details.")
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


# ---------- User Logout ----------
def logout_view(request):
    """Log out the current user."""
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return render(request, 'relationship_app/logout.html')


from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required

def _has_role(user, role_name):
    # If anonymous, user won't have profile attribute; deny access
    if not user.is_authenticated:
        return False
    # In case profile doesn't exist (rare), deny access
    profile = getattr(user, 'profile', None)
    if profile is None:
        return False
    return profile.role == role_name

def _is_admin(user):
    return _has_role(user, 'Admin')

def _is_librarian(user):
    return _has_role(user, 'Librarian')

def _is_member(user):
    return _has_role(user, 'Member')

@user_passes_test(_is_admin, login_url='login')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(_is_librarian, login_url='login')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(_is_member, login_url='login')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm

# Create a book (requires 'can_add_book' permission)
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})


# Edit a book (requires 'can_change_book' permission)
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})


# Delete a book (requires 'can_delete_book' permission)
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})




