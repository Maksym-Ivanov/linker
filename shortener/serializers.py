# # shortener/serializers.py

# from rest_framework import serializers
# from .models import CustomUser, URL
# from django.contrib.auth import get_user_model

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ('id', 'username', 'email', 'gender', 'birth_date', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = get_user_model().objects.create_user(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             gender=validated_data['gender'],
#             birth_date=validated_data['birth_date'],
#             password=validated_data['password']
#         )
#         return user

# class URLSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = URL
#         fields = ('id', 'original_url', 'short_url', 'created_at', 'user')

# shortener/serializers.py

from rest_framework import serializers
from .models import CustomUser, URL

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'gender', 'birth_date', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            gender=validated_data['gender'],
            birth_date=validated_data['birth_date'],
            password=validated_data['password']
        )
        return user

class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ('id', 'original_url', 'short_url', 'created_at', 'user')
        read_only_fields = ('short_url', 'user', 'created_at')  # Додаємо поля, які не потребують введення
