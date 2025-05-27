# # userauth/serializer.py
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']


# userauth/serializer.py
# from rest_framework import serializers
# from .models import CustomUser

# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'date_joined']


# from dj_rest_auth.registration.serializers import RegisterSerializer
# from rest_framework import serializers

# class CustomRegisterSerializer(RegisterSerializer):
#     username = None  # Remove the username field

#     def get_cleaned_data(self):
#         return {
#             'email': self.validated_data.get('email', ''),
#             'password1': self.validated_data.get('password1', ''),
#         }

