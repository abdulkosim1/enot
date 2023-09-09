from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product
from rest_framework.permissions import IsAuthenticated
from account.permissions import IsCompany
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model
from django.db.models import Count

# import logging

# logger = logging.getLogger('main')

User = get_user_model()

class CustomPagination(PageNumberPagination): # Кастомная пагинация
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 20

class ProductListAPIView(generics.ListAPIView): # Просмотр постов 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['owner', 'title', 'likes', 'comments']
    search_fields = ['title', ]
    ordering_fileds = ['id','owner', 'likes', 'comments']

    # logger.info('get all posts')

class ProductCreateAPIView(generics.CreateAPIView): # Добавление постов
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsCompany,]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProductRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView): # Удаление, изменение постов
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsCompany,]
    lookup_field='id'

class SystemOfRecomendation(ListAPIView): # Get запрос на систему рекомендаций  
    serializer_class = ProductSerializer
    permission_classes = []
    pagination_class = CustomPagination
    # queryset = Product.objects.annotate(like_count=Count('likes')).filter(like_count__gt=1)
