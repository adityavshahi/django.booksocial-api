from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from booksocial_api import serializers


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
    def list(self,request):
        test_parameters = ['1',2,3.0]
        return Response({'message': 'Test ViewSet successful','test_parameters': test_parameters})