from rest_framework.views import APIView
from rest_framework.response import Response


class HealthCheckView(APIView):
    """Health check view to determine if the server is up and running ."""
    def get(self,request,format=None):
        return Response({"message": "Server up and running !!"})