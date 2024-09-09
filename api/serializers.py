from rest_framework import serializers
from api.models import Products
from django.contrib.auth.models import User

class ProductSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    price=serializers.IntegerField()
    description=serializers.CharField()
    category=serializers.CharField()
    image=serializers.ImageField(required=False,default=None)

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields='__all__'
        # fields=['name','price'] (not serialize all fields)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']
        
    def create(self, validated_data):
        return User.objects.create_user(**self.validated_data)
    
# read_only -> work any one(serialize / deserialisation)