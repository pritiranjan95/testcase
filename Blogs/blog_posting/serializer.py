from rest_framework import serializers
from .models import Blogmodel


class blogserialzer(serializers.ModelSerializer):
    model=Blogmodel
    fields="__all__"
    