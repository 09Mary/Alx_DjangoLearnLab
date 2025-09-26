from rest_framework import generics, filters
from .models import Book #replace with your working model
from .serializers import BookSerializer # replace with your project's serializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAuthenticated
from django_filters import rest_framework

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

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

# filtering
    filterset_fields = ['title', 'author', 'publication_year'] 

# searching
    search_fields = ['title', 'author']
 
# ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering
