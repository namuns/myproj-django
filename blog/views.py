from rest_framework import viewsets
from blog.serializers import PostSerializers
from blog.models import Post
import json
from django.http import HttpResponse


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


def post_list(request):
    qs = Post.objects.all()
    data = [
            {
                "id": post.id,
                "title": post.title,
                "content": post.content,
            }
            for post in qs
        ]
    json_string = json.dumps(data)
    return HttpResponse(json_string)
