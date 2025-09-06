from django.urls import path
from . import views
from .views import register, CustomLoginView, CustomLogoutView

urlpatterns = [
    # Existing routes for your app
    path("books/", views.list_books, name="list_books"),  
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # Authentication routes
    path("register/", register, name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),

     path("admin-role/", views.admin_view, name="admin_view"),
    path("librarian-role/", views.librarian_view, name="librarian_view"),
    path("member-role/", views.member_view, name="member_view"),

    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # Auth
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    # Role-based
    path("admin-dashboard/", views.admin_view, name="admin_view"),
    path("librarian-dashboard/", views.librarian_view, name="librarian_view"),
    path("member-dashboard/", views.member_view, name="member_view"),

    # Book CRUD (with permissions)
    path("books/add/", views.add_book, name="add_book"),
    path("books/<int:book_id>/edit/", views.edit_book, name="edit_book"),
    path("books/<int:book_id>/delete/", views.delete_book, name="delete_book"),
]
