from django.urls import path
from .views import blog_list, blog_detail, blog_tag, blog_category, Search

app_name = "blogs"

urlpatterns = [
    path('blog/', blog_list),
    path('blog/<int:id>/', blog_detail, name="blog_detail"),
    path("blog/tag/<slug:tag>", blog_tag, name="tag"),
    path("blog/category/<slug:category>", blog_category, name="category"),
    path("blog/search", Search, name="search"),
]