from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from booksocial_api import serializers
from booksocial_api import models
from booksocial_api import permissions


class HealthCheckView(APIView):
    """Health check view to determine if the server is up and running ."""
    def get(self,request,format=None):
        return Response({"message": "Server up and running !!"})


class SayHello(APIView):
    """Say hello to the user ."""
    serializer_class = serializers.SayHelloSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({"message": message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class TestViewSet(viewsets.ViewSet):
    """Testing viewset functionality"""
    serializer_class = serializers.ViewsetSerializer
    def list(self,request):
        test_parameters = ['1',2,3.0]
        return Response({'message': 'Test ViewSet successful','test_parameters': test_parameters})
    

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            first_name = serializer.validated_data.get('first_name')
            last_name = serializer.validated_data.get('last_name')
            age = serializer.validated_data.get('age')
            messsage = f'Hi {first_name} {last_name}. You are {age} years old.'
            return Response({"message": messsage})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email')