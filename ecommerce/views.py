from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from ecommerce.models import Category, Product
from ecommerce.serializers import CategorySerializer, ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from core.pagination import CustomPagination

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):

    filter_backends = [filters.SearchFilter]
    search_fields = ['name','description']

    pagination_class = CustomPagination

    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all() #.order_by('-created_at')
    serializer_class = CategorySerializer
    http_method_names = ['get','post','put','patch','delete']


class ProductViewSet(viewsets.ModelViewSet):

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    permission_classes = []

    queryset = Product.objects.all() #.order_by('id')

    serializer_class = ProductSerializer
    
