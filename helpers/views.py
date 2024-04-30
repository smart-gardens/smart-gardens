from typing import Self, Type

from django.db.models import Model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView

from .managers import BaseManager


class BaseAPIView(APIView):
    class Meta:
        model: Type[Model]
        serializer: Type[ModelSerializer]
        manager: BaseManager

    def get(self: Self, format=None) -> Response:
        return Response(self.Meta.manager.get_list_of_items())

    def post(self: Self, request) -> Response:
        return Response(
            self.Meta.manager.create_item(request.data), status=status.HTTP_201_CREATED
        )
