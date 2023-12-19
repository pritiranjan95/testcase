from django.urls import path, include
from signup import views


urlpatterns = [
    path ("create", view=views.Signup_operations.as_view()),
    path ("users", view=views.Signup_operations.as_view()),
    path("finduser/<str:pk>", view=views.Login.as_view())
]
