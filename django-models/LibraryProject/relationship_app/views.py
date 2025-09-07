from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from .forms import BookForm    # we'll create this form
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.views.generic import DetailView
from .models import Book, Library
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import Library

# ------------------
# Book and Library Views
# ------------------

# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

# ------------------
# Authentication Views
# ------------------

# Register
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# Login
class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"

# Logout
class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"
def is_admin(user):
    return user.userprofile.role == "Admin"

def is_librarian(user):
    return user.userprofile.role == "Librarian"

def is_member(user):
    return user.userprofile.role == "Member"

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")

# ------------------
# Book Management with Custom Permissions
# ------------------

# Add Book (requires "can_add_book" permission)
@permission_required("relationship_app.can_add_book", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully.")
            return redirect("list_books")
    else:
        form = BookForm()
    return render(request, "relationship_app/add_book.html", {"form": form})


# Edit Book (requires "can_change_book" permission)
@permission_required("relationship_app.can_change_book", raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully.")
            return redirect("list_books")
    else:
        form = BookForm(instance=book)
    return render(request, "relationship_app/edit_book.html", {"form": form})


# Delete Book (requires "can_delete_book" permission)
@permission_required("relationship_app.can_delete_book", raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        messages.success(request, "Book deleted successfully.")
        return redirect("list_books")
    return render(request, "relationship_app/delete_book.html", {"book": book})

 