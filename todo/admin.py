from django.contrib import admin
from todo.models import Post


class PostAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_display = ['id', "created_at", "title", "body"]
    list_display_links = ["id", "title"]
    search_fields = ["title", "body", "user"]


admin.site.register(Post, PostAdmin)
