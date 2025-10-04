from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        request.user.email = request.POST.get('email')
        request.user.save()
    return render(request, 'blog/profile.html', {'user': request.user})

# ✅ Show all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'   # create this template
    context_object_name = 'posts'


# ✅ Show details of a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'   # create this template
    context_object_name = 'post'


# ✅ Create a new post
class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'     # create this template
    fields = ['title', 'content']             # adjust to your Post model fields


# ✅ Update/Edit an existing post
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']


# ✅ Delete a post
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'   # create this template
    success_url = reverse_lazy('post-list')
