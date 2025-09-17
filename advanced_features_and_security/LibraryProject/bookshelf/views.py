from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    # logic to create book
    return render(request, "relationship_app/add_book.html")

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # logic to edit book
    return render(request, "relationship_app/edit_book.html", {"book": book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # logic to delete book
    return redirect("list_books")
