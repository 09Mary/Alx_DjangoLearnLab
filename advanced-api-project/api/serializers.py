
from rest_framework import serializers
from .models import Book,Author

# BookSerializer serializes all fields and validates publication_year
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year']

# AuthorSerializer includes nested BookSerializer to show related books
class AuthorSerializer(serializers.ModelSerializer):

    # Nested serializer
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "bio", "books"]  
