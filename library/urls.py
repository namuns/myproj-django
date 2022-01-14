from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library import views
from library.views import BookViewSet
app_name = "library"

router = DefaultRouter()
router.register("books", BookViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    # path("book.json", views.book_list),
]