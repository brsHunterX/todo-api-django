from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from todo.views import UserViewSet, PostViewSet, UserPostsViewSet

router = DefaultRouter()

router.register("users", UserViewSet, basename="Users")
router.register("posts", PostViewSet, basename="Posts")

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path("users/<int:id>/posts/", UserPostsViewSet.as_view())
]
