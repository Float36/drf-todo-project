from rest_framework import serializers
from django.utils.timezone import now
from django.contrib.auth.models import User

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """
    Serializer fot Todo model
    """
    owner_username = serializers.ReadOnlyField(source='owner.username')

    days_since_creation = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'is_completed',
                  'created_at', 'owner_username', 'days_since_creation'
        ]

    def get_days_since_creation(self, obj):
        """
        Повертає кількість днів що пройшли з моменту створення
        :param obj:
        :return:
        """
        return (now() - obj.created_at).days

    def validate_title(self, value):
        """
        Заголовок повинен бути більше 5 символів
        :param value: значення що прийшло у полі title
        :return:
        """
        if len(value) < 5:
            raise serializers.ValidationError("Заголовок має містити мінімум 5 символів")

        return value