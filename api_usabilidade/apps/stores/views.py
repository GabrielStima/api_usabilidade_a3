from rest_framework import viewsets, generics, status
from django.shortcuts import get_object_or_404
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class StoreViewset(APIView):
    queryset = models.Store.objects.all()

    def get(self, request, id=None):
        if id:
            item = models.Store.objects.get(id=id)
            serializer = serializers.StoreSerializer(item)

            return Response({serializer.data}, status=status.HTTP_200_OK)
        
        items = models.Store.objects.all()
        serializer = serializers.StoreSerializer(items, many=True)

        return Response({serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = serializers.StoreSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None):
        item = models.Store.objects.get(id=id)
        serializer = serializers.StoreSerializer(item, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id=None):
        item = models.Store.objects.filter(id=id)
        item.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
class StoreViewset_UUID(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Store.objects.all()
    serializer_class = serializers.StoreSerializer