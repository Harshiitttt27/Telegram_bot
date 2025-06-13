from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def public_api(request):
    return Response({"message": "Public API - anyone can access this."})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_api(request):
    return Response({"message": "Protected API - only authenticated users can access this."})

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TelegramUser

@api_view(['GET'])
def list_telegram_users(request):
    users = TelegramUser.objects.all().values('username', 'registered_at')
    return Response({"users": list(users)})
@api_view(['POST'])
def simulate_start(request):
    username = request.data.get("username")
    if username:
        TelegramUser.objects.get_or_create(username=username)
        return Response({"message": f"{username} registered!"})
    return Response({"error": "Username not provided"}, status=400)
