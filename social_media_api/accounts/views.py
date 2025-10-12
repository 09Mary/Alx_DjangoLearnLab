from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status

from rest_framework.views import APIView

from rest_framework import generics, permissions
from django.conf import settings

from .models import Post
from .serializers import PostSerializer
from rest_framework.pagination import PageNumberPagination

User = get_user_model()

class FeedPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]   # feed is private to logged-in users
    pagination_class = FeedPagination

    def get_queryset(self):
        user = self.request.user

        # optionally include own posts (query param include_self=true|false, default true)
        include_self = self.request.query_params.get('include_self', 'true').lower() in ['1', 'true', 'yes']

        # users the user follows
        following_qs = user.following.all()

        if include_self:
            # include user in authors
            authors = list(following_qs) + [user]
        else:
            authors = list(following_qs)

        return Post.objects.filter(author__in=authors).order_by('-created_at')


class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        if request.user.id == user_id:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        to_follow = get_object_or_404(User, id=user_id)
        request.user.following.add(to_follow)
        return Response({"detail": f"You are now following {to_follow.username}."}, status=status.HTTP_200_OK)


class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        if request.user.id == user_id:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        to_unfollow = get_object_or_404(User, id=user_id)
        request.user.following.remove(to_unfollow)
        return Response({"detail": f"You have unfollowed {to_unfollow.username}."}, status=status.HTTP_200_OK)


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "message": "User registered successfully",
            "username": user.username,
            "token": token.key
        }, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
