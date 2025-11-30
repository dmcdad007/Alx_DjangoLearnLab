from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from api.models import Book, Author


# -----------------------------------------------------------------------
# Test Suite for Book API Endpoints
# -----------------------------------------------------------------------
# Covers:
#   - CRUD operations
#   - Permissions
#   - Filtering
#   - Searching
#   - Ordering
#
# Uses Django’s test database, recreated for each test run.
# -----------------------------------------------------------------------
class BookAPITestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        # Create authors
        cls.author1 = Author.objects.create(name="George Orwell")
        cls.author2 = Author.objects.create(name="J.R.R. Tolkien")

        # Create books
        cls.book1 = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=cls.author1
        )
        cls.book2 = Book.objects.create(
            title="Animal Farm",
            publication_year=1945,
            author=cls.author1
        )
        cls.book3 = Book.objects.create(
            title="The Hobbit",
            publication_year=1937,
            author=cls.author2
        )

        # Create user for authenticated tests
        cls.user = User.objects.create_user(username="testuser", password="password123")

        cls.client = APIClient()


    # -------------------------------------------------------
    # LIST VIEW TESTS
    # -------------------------------------------------------
    def test_list_books(self):
        """Ensure anyone can list all books."""
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)


    def test_filter_books_by_author(self):
        """Test filtering books by author."""
        response = self.client.get(reverse('book-list'), {'author': self.author1.id})
        self.assertEqual(len(response.data), 2)


    def test_search_books(self):
        """Test searching by book title or author name."""
        response = self.client.get(reverse('book-list'), {'search': 'Hobbit'})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "The Hobbit")


    def test_order_books(self):
        """Test ordering books by publication_year descending."""
        response = self.client.get(reverse('book-list'), {'ordering': '-publication_year'})
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))


    # -------------------------------------------------------
    # DETAIL VIEW TEST
    # -------------------------------------------------------
    def test_get_single_book(self):
        response = self.client.get(reverse('book-detail', args=[self.book1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "1984")


    # -------------------------------------------------------
    # CREATE VIEW TESTS
    # -------------------------------------------------------
    def test_create_book_unauthenticated(self):
        """Unauthenticated users cannot create books."""
        payload = {
            "title": "New Book",
            "publication_year": 2000,
            "author": self.author1.id
        }
        response = self.client.post(reverse('book-create'), payload)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_create_book_authenticated(self):
        """Authenticated users can create a book."""
        self.client.login(username='testuser', password='password123')

        payload = {
            "title": "New Book",
            "publication_year": 2000,
            "author": self.author1.id
        }
        response = self.client.post(reverse('book-create'), payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)


    # -------------------------------------------------------
    # UPDATE VIEW TESTS
    # -------------------------------------------------------
    def test_update_book_unauthenticated(self):
        payload = {"title": "Updated Book"}
        response = self.client.patch(reverse('book-update', args=[self.book1.id]), payload)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='password123')

        payload = {"title": "Updated Title"}
        response = self.client.patch(reverse('book-update', args=[self.book1.id]), payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")


    # -------------------------------------------------------
    # DELETE VIEW TESTS
    # -------------------------------------------------------
    def test_delete_book_unauthenticated(self):
        response = self.client.delete(reverse('book-delete', args=[self.book1.id]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='password123')

        response = self.client.delete(reverse('book-delete', args=[self.book1.id]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())
