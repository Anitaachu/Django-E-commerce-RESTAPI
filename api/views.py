from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Category, Book, Clothing, Grocery
from .serializers import CategorySerializer, BookSerializer, ClothingSerializer, GrocerySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Create your views here.

class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None
    filter_backend = [DjangoFilterBackend]
    filterset_fields = {
        "category": ["exact"],
        "book_title": ["exact"],
        "grocery_name": ["exact"],
        "clothing_clothing_choice": ["exact"],
    }

class DetailCategory(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class BookView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = None
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {
        "title": ["exact"]
    }
    search_fields = ['title', 'author']

class DetailBook(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class GroceryView(ListCreateAPIView):
    queryset = Grocery.objects.all()
    serializer_class = GrocerySerializer
    pagination_class = None
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {
        "name": ["exact"]
    }
    search_fields = ['name']

class DetailGrocery(RetrieveUpdateDestroyAPIView):
    queryset = Grocery.objects.all()
    serializer_class = GrocerySerializer


class ClothingView(ListCreateAPIView):
    queryset = Clothing.objects.all()
    serializer_class = ClothingSerializer
    pagination_class = None
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {
        "clothes": ["exact"]
    }
    search_fields = ['clothes']