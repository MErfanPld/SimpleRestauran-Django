from django.contrib import admin
from .models import Blog, Category, Tag, Comments

# Register your models here.


#=====================BlogAdmin=====================

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "author")
    list_filter = ("created_at",)
    search_fields = ("title",)
    ordering = ("title", "author", "created_at")
    date_hierarchy = "author__date_joined"

admin.site.register(Blog,BlogAdmin),




#=====================CategoryAdmin=====================

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "published_at")
    list_filter = ("title",)
    search_fields = ("title","slug","published_at")
    ordering = ("title", "slug", "published_at")

admin.site.register(Category,CategoryAdmin),





#=====================BlogAdmin=====================

class TagAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "update_at")
    list_filter = ("title",)
    search_fields = ("title","slug","update_at")
    ordering = ("title", "slug", "update_at")

admin.site.register(Tag,TagAdmin),




#=====================CommentsAdmin=====================

class CommentsAdmin(admin.ModelAdmin):
    list_display = ("blog", "fullname", "email", "date")
    list_filter = ("blog",)
    search_fields = ("blog","fullname","email")
    ordering = ("blog", "fullname", "email", "date")

admin.site.register(Comments,CommentsAdmin),
