from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import PostViewSet, post_list, post_create

app_name = 'blog'

router = DefaultRouter()
router.register("posts", PostViewSet)

urlpatterns = [
    path("/blog/", post_list, name="post_list"),
    path("blog/:postId/", post_create, name="post_create"),
    # path("blog/:postId/edit/", blog_edit, name="blog_edit"),
    path("api/", include(router.urls)),
]