from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, LikePostView, UnlikePostView
from .views import FeedView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

# Nested route for comments under posts
comments_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
comments_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='post-like'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='post-unlike'),
    path('posts/<int:post_pk>/comments/', comments_list, name='comment-list'),
    path('posts/<int:post_pk>/comments/<int:pk>/', comments_detail, name='comment-detail'),
    path('feed/', FeedView.as_view(), name='feed'),
    path('posts/<int:post_pk>/comments/', ...), 
]
