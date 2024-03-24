from typing import Self

from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator


class UserSerializer(ModelSerializer):
    def create(self: Self, validated_data: dict[str, str]) -> User:
        """Create

        Create a new user based on the data received
        """
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(), fields=["username", "email"]
            )
        ]
