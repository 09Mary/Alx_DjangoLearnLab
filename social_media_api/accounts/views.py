from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import CustomUser
from notifications.utils import create_notification

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@login_required
def follow_user(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)
    if target_user != request.user:
        request.user.following.add(target_user)
        create_notification(recipient=target_user, actor=request.user, verb='started following you', target=target_user)
        return JsonResponse({'status': 'followed'})
    return JsonResponse({'status': 'cannot follow yourself'})

@login_required
def unfollow_user(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)
    request.user.following.remove(target_user)
    return JsonResponse({'status': 'unfollowed'})
       