# shortener/views.py

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect
from .models import URL
from .serializers import UserSerializer, URLSerializer
from django.contrib.auth import get_user_model
import string, random

class UserCreate(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class URLListCreate(generics.ListCreateAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        serializer.save(user=self.request.user, short_url=short_url)

class UserURLs(generics.ListAPIView):
    serializer_class = URLSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return URL.objects.filter(user=self.request.user)

def redirect_to_original(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)
    return redirect(url.original_url)
