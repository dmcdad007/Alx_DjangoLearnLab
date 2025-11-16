from django.shortcuts import render
from .forms import ExampleForm

# Create your views here.

# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Article
from .forms import ArticleForm  # assume you have a ModelForm


# ----------------------------------------------------------------------
# Helper: common 403 page
# ----------------------------------------------------------------------
def permission_denied_view(request, exception):
    return render(request, '403.html', status=403)


# ----------------------------------------------------------------------
# LIST – only users with `can_view` may see the list
# ----------------------------------------------------------------------
@login_required
@permission_required('blog.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles})


# ----------------------------------------------------------------------
# CREATE
# ----------------------------------------------------------------------
@login_required
@permission_required('blog.can_create', raise_exception=True)
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, 'Article created.')
            return redirect('blog:article_list')
    else:
        form = ArticleForm()
    return render(request, 'blog/article_form.html', {'form': form, 'action': 'Create'})


# ----------------------------------------------------------------------
# UPDATE
# ----------------------------------------------------------------------
@login_required
@permission_required('blog.can_edit', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article updated.')
            return redirect('blog:article_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/article_form.html', {'form': form, 'action': 'Edit'})


# ----------------------------------------------------------------------
# DELETE
# ----------------------------------------------------------------------
@login_required
@permission_required('blog.can_delete', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        messages.success(request, 'Article deleted.')
        return redirect('blog:article_list')
    return render(request, 'blog/article_confirm_delete.html', {'article': article})

book_list", "books

# bookshelf/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Book
from .forms import BookReviewForm  # Assume you have this form


def book_list(request):
    """
    Secure search: Use Q objects to prevent SQL injection.
    Always validate and sanitize user input.
    """
    query = request.GET.get('q', '').strip()
    books = Book.objects.all()

    if query:
        # Safe parameterized query using ORM
        books = books.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query)
        )

    return render(request, 'bookshelf/book_list.html', {
        'books': books,
        'query': query
    })


def add_review(request, book_id):
    """
    Secure form handling:
    - Use Django Form for validation
    - CSRF enforced by template
    - No raw SQL
    """
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        form = BookReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            messages.success(request, 'Review added successfully.')
            return redirect('bookshelf:book_list')
    else:
        form = BookReviewForm()

    return render(request, 'bookshelf/form_example.html', {
        'form': form,
        'book': book
    })


