from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Todo
from .serializers import TodoSerializer
from .permissions import IsOwnerOrReadOnly


class TodoListCreateView(generics.ListCreateAPIView):
    """
    GET for all tasks, POST for new task
    """
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer

    def get_queryset(self):
        """
        Return list of tasks for authenticated user
        """
        user = self.request.user
        return Todo.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET PUT PATCH DELETE by id
    """
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


    queryset = Todo.objects.all()
    serializer_class = TodoSerializer



