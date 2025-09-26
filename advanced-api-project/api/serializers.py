
from rest_framework import serializers, generics
from .models import Book,Author

# BookSerializer serializes all fields and validates publication_year
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year']

#custom for publication year  
    def validate(self, data):
        if len(data['publication_year']) < 5:
            raise serializers.ValidationError("publication year can not be future.")
        return data     

# AuthorSerializer includes nested BookSerializer to show related books
class AuthorSerializer(serializers.ModelSerializer):

    # Nested serializer
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "bio", "books"]  

class BookCreatView(generics.CreateAPIView):

    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
class BookUpdateView(generics.CreateAPIView):

    def check_permissions(self, request):
        return super().check_permissions(request)   


