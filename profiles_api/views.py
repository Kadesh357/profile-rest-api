from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """TEST API VIEW"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """"Returns a list of APIView Features"""
        an_apiview = [
            'Uses HTTP methods (get,post,patch,put,delete)',
            'Is Similar to a traditional Django View',
            'Aadesh is Great ',
            'URL mapping manually to URLs',
        ]

        return Response({'message':'Hello1!','an_apiview': an_apiview})

    def post(self,request):
        """Create a hello message with our Name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            msg= f'Hello {name}'
            return Response({'message': msg})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handle updating object"""
        return Response({'method' : 'PUT'})

    def patch(self,request,pk=None):
        """Handle a partial update of an object"""
        return Response({'method' : 'PATCH'})

    def delete(self,request,pk=None):
        """Handle a delete and of an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class =serializers.HelloSerializer

    def list(self, request):
        """Return a Hello message """
        a_viewset =[
            'User actions (list,create,retrieve,update,partial+update)',
            'Automatically maps to URLs using Routers',
            'Providers more funtionality with less code'

        ]

        return Response({'message ':'Hello!','a_viewset':a_viewset})

    def create(self,request):
        """Create a new hello message"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status =status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """Handle Getting an object by its ID"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handle updating an object by its ID"""
        return Response({'http_method':'PUT'})

    def patch(self,request,pk=None):
        """Handle partial updating an object by its ID"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Handle deleteing an object by its ID"""
        return Response({'http_method':'DELETE'})


class  UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profile"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes =(permissions.UpdateOwnProfile,)
