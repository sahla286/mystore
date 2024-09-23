from rest_framework import serializers
from api.models import Products,Carts,Reviews
from django.contrib.auth.models import User

# class ProductSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField()
#     price=serializers.IntegerField()
#     description=serializers.CharField()
#     category=serializers.CharField()
#     image=serializers.ImageField(required=False,default=None)

class ProductModelSerializer(serializers.ModelSerializer):
    avg_rating=serializers.CharField(read_only=True)
    review_count=serializers.CharField(read_only=True)
    class Meta:
        model=Products
        fields='__all__'
        # fields=['name','price'] (not serialize all fields)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']
        
    def create(self,validated_data):
        return User.objects.create_user(**self.validated_data)
    
class CartSerializer(serializers.ModelSerializer):

    id=serializers.IntegerField(read_only=True) # only seralization
    user=serializers.CharField(read_only=True) 
    product=serializers.CharField(read_only=True) 
    date=serializers.CharField(read_only=True)

    class Meta:
        model=Carts
        fields='__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True) 
    product=serializers.CharField(read_only=True) 
    date=serializers.CharField(read_only=True)

    class Meta:
        model=Reviews
        fields='__all__'
    
# read_only -> work any one(serialize / deserialisation)