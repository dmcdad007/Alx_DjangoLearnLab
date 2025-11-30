from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# BookSerializer handles serialization and validation for Book objects.
# It includes custom validation to ensure publication_year is not in the future.
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validator to ensure publication year is not in the future.
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


# AuthorSerializer serializes Author objects.
# It includes a nested serializer to automatically serialize related books.
#
# books: This field is nested and read-only by default.
#        It shows each book using the BookSerializer.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
