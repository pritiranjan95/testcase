from django.shortcuts import render
from .models import Signup
from .serializer import SignupSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class Signup_operations(APIView):
    def post(self, request):
        try:
            s=SignupSerializer(data=request.data)
            if s.is_valid():
                s.save()
                return Response(s.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"details": {e}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(self, request):
        s=Signup.objects.all()
        serializer=SignupSerializer(s,many=True)
        return Response(serializer.data)
    
 #We have to send the email-id of the user with the api to login    
class Login(APIView):    
    def get(self, request, pk=None):
        try:
            s=Signup.objects.get(Email_id=pk)
            if s:
                return Response({"details":"Successfully logedIn"}, status=status.HTTP_200_OK)
            else:
                return Response({"details": "Please signup first"})
        except Exception as e:
            return Response({"details":{e}})
        

        