from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Products
from api.serializers import ProductSerializer

# Create your views here.

class ProductView(APIView):
    def get(self,request,*args,**kw):
        qs=Products.objects.all()
        serializer = ProductSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def post(self,request,*args,**kw):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            Products.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer._errors)
    
class ProductDetailsView(APIView):
    def get(self,request,*args,**kw):
        id = kw.get('id')
        qs=Products.objects.get(id=id)
        serializer = ProductSerializer(qs)
        return Response(data=serializer.data)
    
    def put(self,request,*args,**kw):
        id = kw.get('id')
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            id = kw.get('id')
            Products.objects.filter(id=id).update(**request.data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer._errors)
    
    def delete(self,request,*args,**kw):
        id = kw.get('id')
        Products.objects.filter(id=id).delete()
        return Response(data='Item deleted')


# seralizers(serialization)

