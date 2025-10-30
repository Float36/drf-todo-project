from django.urls import path
from . import views2


urlpatterns = [
    path('todos/', views2.TodoListCreateView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>', views2.TodoDetailView.as_view(), name='todo-detail'),
]