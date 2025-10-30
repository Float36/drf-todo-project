from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """
    Serializer fot Todo model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'is_completed', 'created_at']
