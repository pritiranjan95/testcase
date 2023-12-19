from .models import Signup
from rest_framework import serializers

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Signup
        fields="__all__"
        