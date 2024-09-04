from rest_framework import serializers
from api.models import Products

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

        
# read_only -> work any one(serialize / deserialisation)