from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class CustomerViewset(APIView):
    def get(self, request, id=None):
        if id:
            item = models. Customer.objects.get(id=id)
            serializer = serializers.CustomerSerializer (item)

            return Response({
                "status": "success",
                "data": serializer.data}, status=status.HTTP_200_OK)
        
        items = models.Customer.objects.all()
        serializer = serializers.CustomerSerializer(items, many=True)

        return Response({
            "status:":"success",
            "data":serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = serializers.CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "status":"success",
                "data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({
                "status":"error",
                "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None):
        item = models.Customer.objects.get(id=id)
        serializer = serializers.CustomerSerializer(item, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "status":"success",
                "data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({
                "status":"error",
                "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id=None):
        item = models.Customer.objects.filter(id=id)
        item.delete()

        return Response({
            "status":"success",
            "data":"Item Deleted"
        })
 