from rest_framework import serializers
from .models import Book,Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year']

class AuthorSerializer(serializers.ModelSerializer):

    # Nested serializer
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "bio", "books"]  