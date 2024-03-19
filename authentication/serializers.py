from django.contrib.auth import authenticate
from rest_framework import serializers

from django.contrib.auth import get_user_model
User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    password = serializers.CharField(
        max_length=255,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password')
    
    def create(self, validated_data):
     
        password = validated_data.pop('password', None)
        if validated_data.get('username') is None:
            raise TypeError("Users must have a username")
        if validated_data.get('email') is None:
            raise TypeError("Users must have an email address")
        user = self.Meta.model(
            **validated_data
        )
        user.set_password(password)
        user.save()

        return user

class LoginSerializer(serializers.ModelSerializer):
    """Serializer login requests and signin user"""
    email = serializers.CharField(max_length=255, read_only=True)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)
    
    class Meta:
        model = User
        fields = ('token','username', 'email', 'password')

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError(
                'A username is required to login'
            )
        if password is None:
            raise serializers.ValidationError(
                'A password is required to login'
            )
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with that username or password was not found'
            )
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated'
            )
        
        return {
            "username": user.username,
            "email": user.email,
            "token": user.token
        }

