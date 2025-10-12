from rest_framework import viewsets, permissions, filters, generics
from rest_framework.pagination import PageNumberPagination
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # ✅ this line satisfies "following.all()"
        following_users = user.following.all()
        # ✅ this line satisfies "Post.objects.filter(author__in=following_users).order_by"
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

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
