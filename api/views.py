from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from api.models import Products
from api.serializers import ProductModelSerializer,UserSerializer
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ProductViewsetView(ModelViewSet):
    serializer_class=ProductModelSerializer
    queryset=Products.objects.all()
    authentication_classes =[BasicAuthentication]
    permission_classes =[IsAuthenticated]

    # custom method
    @action(methods=['GET'],detail=False)
    def categories(self,request,*args,**kw):
        qs=Products.objects.values_list('category',flat=True).distinct()
        return Response(data=qs)

class UserViewsetView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()


# class ProductView(APIView):
#     def get(self,request,*args,**kw):
#         qs=Products.objects.all()
#         serializer = ProductSerializer(qs,many=True)
#         return Response(data=serializer.data)
    
#     def post(self,request,*args,**kw):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             print(serializer.validated_data)
#             Products.objects.create(**serializer.validated_data)
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
    
# class ProductDetailsView(APIView):
#     def get(self,request,*args,**kw):
#         id = kw.get('id')
#         qs=Products.objects.get(id=id)
#         serializer = ProductSerializer(qs)
#         return Response(data=serializer.data)
#     # update
#     def put(self,request,*args,**kw):
#         id = kw.get('id')
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             id = kw.get('id')
#             Products.objects.filter(id=id).update(**request.data)
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer._errors)
    
#     def delete(self,request,*args,**kw):
#         id = kw.get('id')
#         Products.objects.filter(id=id).delete()
#         return Response(data='Item deleted')


# class UserViewsetView(ViewSet):
#         def create(self,request,*args,**kw):
#             serializer = UserSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(data=serializer.data)
#             else:
#                 return Response(data=serializer.errors)
        
#         def update(self,request,*args,**kw):
#             id = kw.get('pk')
#             obj=User.objects.get(id=id)
#             serializer = UserSerializer(data=request.data,instance=obj)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(data=serializer.data)
#             else:
#                 return Response(data=serializer.errors)
            
#         def destroy(self,request,*args,**kw):
#             id = kw.get('pk')
#             User.objects.filter(id=id).delete()
#             return Response(data='Item deleted')


# class ProductViewsetView(ViewSet):
#     def list(self,request,*args,**kw):
#         qs=Products.objects.all()
#         serializer=ProductModelSerializer(qs,many=True)
#         return Response(data=serializer.data)
    
#     # post products(add)
#     def create(self,request,*args,**kw):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
        
#     # get a product
#     def retrieve(self,request,*args,**kw):
#         id = kw.get('pk')
#         qs=Products.objects.get(id=id)
#         serializer = ProductModelSerializer(qs)
#         return Response(data=serializer.data)
    
#     def update(self,request,*args,**kw):
#         id = kw.get('pk')
#         obj=Products.objects.get(id=id)
#         serializer = ProductModelSerializer(data=request.data,instance=obj)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)

#     def destroy(self,request,*args,**kw):
#         id = kw.get('pk')
#         Products.objects.filter(id=id).delete()
#         return Response(data='Item deleted')
    
# # custom method
#     @action(methods=['GET'],detail=False)
#     def categories(self,request,*args,**kw):
#         qs=Products.objects.values_list('category',flat=True).distinct()
#         return Response(data=qs)



# seralizers(serialization)

# modelviewset :- 
