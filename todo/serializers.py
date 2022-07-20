from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User
from todo.models import Task


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "username", "password"]


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "created_at", "user", "title", "body"]


# class UserTasksSerializer(ModelSerializer):
#     created_by = SerializerMethodField()

#     def get_created_by(self, obj):
#         return f"{obj.user.first_name} {obj.user.last_name}"

#     class Meta:
#         model = Task
#         fields = ["id", "created_at", "created_by", "title", "body"]
