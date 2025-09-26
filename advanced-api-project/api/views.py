from rest_framework import generics
from .models import Book #replace with your working model
from .serializers import BookSerializer # replace with your project's serializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAuthenticated

class BookCreateView(generics.CreateAPIView):
# can be any name, ensure to align with your project as this is sample exampls 
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer    