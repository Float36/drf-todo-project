from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Todo
from .serializers import TodoSerializer
from .permissions import IsOwnerOrReadOnly


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def get_queryset(self):
        """
        Return tasks only for current user
        :return:
        """
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """
        Призначає поточного користувача власником таски при створенні нового завдання.
        :param serializer:
        :return:
        """
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        """
        Призначає різні дозволи для різних дій
        :return:
        """
        if self.action == 'list' or self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

        return [permission() for permission in permission_classes]
