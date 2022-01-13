from rest_framework import viewsets
from blog.models import Post
import json
from django.http import HttpResponse
from library.serializers import LibrarySerializers


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = LibrarySerializers


def library_list(request):
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