from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """TEST API VIEW"""

    def get(self, request, format=None):
        """"Returns a list of APIView Features"""
        an_apiview = [
            'Uses HTTP methods (get,post,patch,put,delete)',
            'Is Similar to a traditional Django View',
            'Aadesh is Great ',
            'URL mapping manually to URLs',
        ]

        return Response({'message':'Hello1!','an_apiview': an_apiview})
