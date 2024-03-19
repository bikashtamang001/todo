from rest_framework import serializers

from . models import Product,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:

        model = Category
        fields = ('name','description')

class ProductSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(max_length=None, allow_empty_file=False,allow_null=True)

    class Meta:
        model = Product
        fields = ('id','name','description','created_at')