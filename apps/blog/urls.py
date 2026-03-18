from django.urls import path

from apps.blog.views import BlogListView, BlogSingleView


urlpatterns = [
    path("posts/", BlogListView.as_view(), name="blogs"),
    path("posts/<slug:slug>/", BlogSingleView.as_view(), name="blog-single"),
]
