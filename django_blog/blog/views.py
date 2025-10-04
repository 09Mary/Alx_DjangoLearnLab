from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

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
