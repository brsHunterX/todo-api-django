from django.contrib.auth.models import User

from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

from todo.models import Post
from todo.serializers import UserSerializer, PostSerializer, UserPostsSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]


class UserPostsViewSet(generics.ListAPIView):
    serializer_class = UserPostsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    def get_queryset(self):
        queryset = Post.objects.filter(user=self.kwargs["id"])
        return queryset
