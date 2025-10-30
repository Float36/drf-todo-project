from django.shortcuts import render
from rest_framework import generics

from .models import Todo
from .serializers import TodoSerializer


class TodoListCreateView(generics.ListCreateAPIView):
    """
    GET for all tasks, POST for new task
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET PUT PATCH DELETE by id
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer



