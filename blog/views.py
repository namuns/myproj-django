from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from rest_framework import viewsets

from blog.forms import PostForm
from blog.serializers import PostSerializer
from blog.models import Post
from rest_framework import viewsets

post_list = ListView.as_view(model=Post)

post_create = CreateView.as_view(
    model=Post,
    form_class=PostForm,
    success_url=reverse_lazy("blog:post_create"),
)

# blog_edit = UpdateView.as_view()



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
