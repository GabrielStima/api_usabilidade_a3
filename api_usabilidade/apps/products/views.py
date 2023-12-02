from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class ProductViewset(APIView):
    def get(self, request, uuid=None):
        if uuid:
            item = models. Product.objects.get(uuid=uuid)
            serializer = serializers.ProductSerializer (item)

            return Response({
                "status": "success",
                "data": serializer.data}, status=status.HTTP_200_OK)
        
        items = models.Product.objects.all()
        serializer = serializers.ProductSerializer(items, many=True)

        return Response({
            "status:":"success",
            "data":serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = serializers.ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "status":"success",
                "data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({
                "status":"error",
                "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, uuid=None):
        item = models.Product.objects.get(uuid=uuid)
        serializer = serializers.ProductSerializer(item, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "status":"success",
                "data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({
                "status":"error",
                "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, uuid=None):
        item = models.Product.objects.filter(uuid=uuid)
        item.delete()

        return Response({
            "status":"success",
            "data":"Item Deleted"
        })
 