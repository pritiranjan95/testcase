from django.urls import path
from . import views

urlpatterns = [
    path("/blogposting", view=views.Blogcreation.as_view())
]
