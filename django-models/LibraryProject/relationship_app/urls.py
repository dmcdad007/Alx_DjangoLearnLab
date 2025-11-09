from django.urls import path
from .views import list_books
from django.urls import path
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
]

from django.urls import path
from .import views

urlpatterns = [
    # Existing routes
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication routes
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('logout/', LogoutView.as_view(template_name="),
    path('login/', LoginView.as_view(template_name="),
    path('register/', views.register_view, name='register'),
     "LoginView.as_view(template_name="
]



urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]
