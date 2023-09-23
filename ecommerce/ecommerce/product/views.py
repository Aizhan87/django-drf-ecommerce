from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from django.db import connection
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import SqlLexer
from sqlparse import format
from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer



class CategoryView(viewsets.ViewSet):
    queryset = Category.objects.all()
    
    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        """
        A simple Viewset for viewing all categories
        """
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    
    
class BrandView(viewsets.ViewSet):
    queryset = Brand.objects.all()
    
    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        """
        A simple Viewset for viewing all brands
        """
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    
    
class ProductView(viewsets.ViewSet):
    queryset = Product.objects.all().isactive() #use isactive from Product model
    lookup_field = 'slug'
    
    def retrieve(self, request, slug=None):
        serializer = ProductSerializer(self.queryset.filter(slug=slug).select_related('category', 'brand'), many=True)
        data = Response(serializer.data)
        # q = list(connection.queries)
        # print(len(q))
        
        # for qs in q:
        #     sqlformatted = format(str(qs['sql']), reindent=True)
        #     print(highlight(sqlformatted, SqlLexer(), TerminalFormatter()))
        return data
    
    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        """
        A simple Viewset for viewing all products
        """
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    @action(methods=['get'], detail=False, url_path=r"category/(?P<category>\w+)/all")
    def list_product_by_category(self, request, category=None):
        """
        An endpoint to return products by category
        """
        serializer = ProductSerializer(self.queryset.filter(category__name=category), many=True)
        return Response(serializer.data)
    