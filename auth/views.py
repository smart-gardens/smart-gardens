from typing import Self

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class UserRecordView(APIView):
    """User Record View

    Create users or get a list of registered users
    """

    permission_classes = [IsAdminUser]

    def get(self: Self, format=None) -> Response:
        """GET

        Get list of all register users
        """
        return Response(UserSerializer(User.objects.all(), many=True).data)

    def post(self: Self, request) -> Response:
        """POST

        Create a new user

        Returns:
            Response: Either an error containing the error message, or the newly created
                user
        """
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=ValueError):  # type: ignore
            return Response(
                {
                    "error": True,
                    "message": serializer.error_messages,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer.create(validated_data=request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
