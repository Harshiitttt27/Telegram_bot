from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from .models import TelegramUser

##public_api
@api_view(['GET'])
def public_api(request):
    return Response({"message": "Public API - anyone can access this."})

# Protected API that requires authentication
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_api(request):
    return Response({"message": "Protected API - only authenticated users can access this."})

# List all Telegram users
@api_view(['GET'])
def list_telegram_users(request):
    users = TelegramUser.objects.all().values('username', 'registered_at')
    return Response({"users": list(users)})

# Simulate a start command for the Telegram bot
@api_view(['POST'])
def simulate_start(request):
    username = request.data.get("username")
    if username:
        TelegramUser.objects.get_or_create(username=username)
        return Response({"message": f"{username} registered!"})
    return Response({"error": "Username not provided"}, status=400)
