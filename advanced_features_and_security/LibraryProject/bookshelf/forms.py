from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
from django import forms
from .models import Book

# Example form for demonstration (used in form_example.html)
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")
    message = forms.CharField(widget=forms.Textarea, label="Message")


# Form for Book model (used in add/edit book views)
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]
