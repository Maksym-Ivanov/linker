# url_shortener/urls.py

from django.contrib import admin
from django.urls import path
from shortener.views import UserCreate, URLListCreate, UserURLs, redirect_to_original
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', UserCreate.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/urls/', URLListCreate.as_view(), name='url_list_create'),
    path('api/user/urls/', UserURLs.as_view(), name='user_urls'),
    path('<str:short_url>/', redirect_to_original, name='redirect_to_original'),
]
