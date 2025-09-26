from django.urls import path
from .views import (
    BookListView, BookCreateView, BookDetailView,
    BookDeleteView, BookUpdateView
)
urlpatterns = [
    path('books/update/<int:id>/', views.update_book, name='update_book'),
    path('books/delete/<int:id>/', views.delete_book, name='delete_book'),
    path('books/create/<int:id>/', views.delete_book, name='create_book'),

]