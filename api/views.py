from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from api.models import Products,Carts,Reviews
from api.serializers import ProductModelSerializer,UserSerializer,CartSerializer,ReviewSerializer
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

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
    
    @action(methods=['POST'],detail=True)
    def add_cart(self,request,*args,**kw):
        id = kw.get('pk')
        user=request.user
        item=Products.objects.get(id=id)
        user.carts_set.create(product=item)
        return Response(data='Item successfully added to cart')
    
    @action(methods=['POST'],detail=True)
    def add_review(self,request,*args,**kw):
        id=kw.get('pk')
        user=request.user
        product=self.queryset.get(id=id)
        ser=ReviewSerializer(data=request.data)
        if ser.is_valid():
            ser.save(product=product,user=user)
            return Response(data=ser.data,status=status.HTTP_201_CREATED)
        return Response(data=ser.errors,status=status.HTTP_400_BAD_REQUEST)
    

      
    # @action(methods=['GET'], detail=True)
    # def retrieve_cart(self, request, *args, **kw):
    #     user = request.user
    #     id = kw.get('pk')
    #     product = Products.objects.get(id=id)
    #     cart_item=user.carts_set.filter(product=product).first()
    #     return Response(data=cart_item)

    
# class CartView(APIView):
#     authentication_classes =[BasicAuthentication]
#     permission_classes =[IsAuthenticated]
#     def post(self, request, *args, **kw):
#         id = kw.get('id')
#         user = request.user
#         item = Products.objects.get(id=id) 
#         Carts.objects.create(user=user, product=item)
#         return Response(data='Item successfully added to cart')

class CartView(ModelViewSet):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Carts.objects.all()
    serializer_class=CartSerializer
    def list(self, request, *args, **kwargs):
        user=request.user
        print(user)
        carts=self.queryset.filter(user=user)
        ser=self.serializer_class(carts,many=True)
        return Response(data=ser.data,status=status.HTTP_200_OK)

class ReviewView(ModelViewSet):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Reviews.objects.all()
    serializer_class=ReviewSerializer
    def list(self, request, *args, **kwargs):
        user=request.user
        print(user)
        reviews=self.queryset.filter(user=user)
        ser=self.serializer_class(reviews,many=True)
        return Response(data=ser.data,status=status.HTTP_200_OK)

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

