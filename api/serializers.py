from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    price=serializers.IntegerField()
    description=serializers.CharField()
    category=serializers.CharField()
    image=serializers.ImageField(required=False,default=None)
# read_only -> work any one(serialize / deserialisation)