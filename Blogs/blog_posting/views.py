from django.shortcuts import render
from rest_framework import status
from .models import Blogmodel
from .serializer import blogserialzer
from rest_framework.views import APIView
from rest_framework.response import Response

class Blogcreation(APIView):
    def post(self, request):
        try:
            s=blogserialzer(data=request.data)
            if s.is_valid():
                s.save()
                return Response(s.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"details": {e}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(self, request, pk=None):
        try:
            if pk is None:
                s=Blogmodel.objects.all()
                serializer=blogserialzer(s, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                s=Blogmodel.objects.get(unique_id=pk)
                serializer=blogserialzer(s)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"details": {e}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        