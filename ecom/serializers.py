from rest_framework import serializers
from .models import Category, SubCategory, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    subcategory = SubCategorySerializer()
    
    class Meta:
        model = Product
        fields = '__all__'
