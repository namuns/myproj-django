from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library import views
from library.views import LibraryViewSet
app_name = "blog"

router = DefaultRouter()
router.register("library", LibraryViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("librarys.json", views.library_list),
]