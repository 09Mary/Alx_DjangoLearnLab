from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from blog.models import Post
from .models import Comment
from .models import Post
from taggit.forms import TagWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),  # ✅ Use TagWidget for better tag input
        }



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    class PostForm(forms.ModelForm):
      class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add your comment...'}),
        }

