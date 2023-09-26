from rest_framework import serializers
from .models import Brand, Category, Product, ProductLine, ProductImage, Attribute, AttributeValue


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


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ['id', 'productline']
        

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ['id','name']
        
        
class AttributeValueSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer(many=False)
    class Meta:
        model = AttributeValue
        fields = ['attribute', 'attribute_value']
        
        
class ProductLineSerializer(serializers.ModelSerializer):
    # product_image = ProductImageSerializer(many=True)
    attribute_value = AttributeValueSerializer(many=True)
    class Meta:
        model = ProductLine
        fields = ['price', 'sku', 'stock_qty', 'order', 'product_image', 'attribute_value']
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        av_data = data.pop('attribute_value')
        attr_values = {}
        for key in av_data:
            attr_values.update({key['attribute']['id']: key['attribute_value']})
        data.update({'specification': attr_values})
        return data
        
             
class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name') #source from brand table column=name and flatten it to display as brand_name
    category_name = serializers.CharField(source='category.name') #source from category table column=name and flatten it to display as category_name
    product_line = ProductLineSerializer(many=True)
    
    class Meta:
        model = Product
        fields = ['name', 'slug', 'description', 'brand_name', 'category_name', 'product_line']
