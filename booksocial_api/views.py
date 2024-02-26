from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from booksocial_api import serializers


class HealthCheckView(APIView):
    """Health check view to determine if the server is up and running ."""
    serializer_class = serializers.HealthCheckSerializer
    def get(self,request,format=None):
        return Response({"message": "Server up and running !!"})
    

    def post(self,request):
        """Post method for testing the server ."""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name} !!'
            return Response({"message": message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)