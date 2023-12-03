from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class UserViewset(APIView):
    def get(self, request, id=None):
        if id:
            item = models. User.objects.get(id=id)
            serializer = serializers.UserSerializer (item)

            return Response({serializer.data}, status=status.HTTP_200_OK)
        
        items = models.User.objects.all()
        serializer = serializers.UserSerializer(items, many=True)

        return Response({serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None):
        item = models.User.objects.get(id=id)
        serializer = serializers.UserSerializer(item, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id=None):
        item = models.User.objects.filter(id=id)
        item.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
 