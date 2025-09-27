from django.urls import path
from .import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/update/<int:id>/', views.update_book, name='update_book'),
    path('books/delete/<int:id>/', views.delete_book, name='delete_book'),
    path('books/create/<int:id>/', views.delete_book, name='create_book'),

]