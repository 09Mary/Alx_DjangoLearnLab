from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

# --- Custom permission ---
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read-only methods for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only owner can edit or delete
        return obj.author == request.user


# --- Pagination ---
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20


# --- Post ViewSet ---
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by('-created_at')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# --- Comment ViewSet ---
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        # Return comments for a specific post if post_id in URL
        post_id = self.kwargs.get('post_pk')
        if post_id:
            return Comment.objects.filter(post_id=post_id).order_by('-created_at')
        return Comment.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        # Assign author and link to post
        post_id = self.kwargs.get('post_pk')
        serializer.save(author=self.request.user, post_id=post_id)
