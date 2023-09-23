from rest_framework import serializers

from .models import Brand, Category, Product, ProductLine

class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='name') #change name to category_name
    class Meta:
        model = Category
        fields = ['category_name']
        
class BrandSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='name') #change name to brand_name
    class Meta:
        model = Brand
        fields = ['brand_name']
   
        
class ProductLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        exclude = ['id', 'product', 'is_active']
        
             
class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name') #source from brand table column name and flatten it to display as brand_name
    category_name = serializers.CharField(source='category.name') #source from category table column name and flatten it to display as category_name
    product_line = ProductLineSerializer(many=True)
    
    class Meta:
        model = Product
        fields = ['name', 'slug', 'description', 'brand_name', 'category_name', 'product_line']
