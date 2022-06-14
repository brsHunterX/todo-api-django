from rest_framework import serializers

from django.contrib.auth.models import User
from todo.models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "username", "password"]


class PostSerializer(serializers.ModelSerializer):
    # user_id = serializers.SerializerMethodField()
    #
    # def get_user_id(self, obj):
    #     return obj.user.id

    class Meta:
        model = Post
        fields = ["id", "created_at", "user", "title", "body", "color"]


class UserPostsSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()

    def get_created_by(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    class Meta:
        model = Post
        fields = ["id", "created_at", "created_by", "title", "body", "color"]
