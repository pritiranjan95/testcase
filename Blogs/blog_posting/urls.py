from django.urls import path

urlpatterns = [
    path("blog", include("blog_posting.urls"))
]
