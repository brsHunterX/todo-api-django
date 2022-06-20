from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from todo.views import UserViewSet, TaskViewSet, UserTasksViewSet

router = DefaultRouter()

router.register("users", UserViewSet, basename="Users")
router.register("tasks", TaskViewSet, basename="Tasks")

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path("users/<int:id>/tasks/", UserTasksViewSet.as_view())
]
