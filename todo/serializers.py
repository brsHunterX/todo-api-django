from rest_framework import serializers

from django.contrib.auth.models import User
from todo.models import Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "username", "password"]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "created_at", "user", "title", "body"]


class UserTasksSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()

    def get_created_by(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    class Meta:
        model = Task
        fields = ["id", "created_at", "created_by", "title", "body"]
