from rest_framework import serializers
from . models import Category, Book, Grocery, Clothing

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = (
            'id',
            'title'
        )
        model = Category

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        fields= (
            'id',
            'title',
            'author',
            'category',
            'isbn',
            'pages', 
            'price',
            'quantity', 
            'description',
            'imageurl',
            'status',
            'date_created',
        )
        model = Book

class GrocerySerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'name',
            'category',
            'price',
            'quantity',
            'imageurl',
            'status',
            'date_created',
        )
        model = Grocery


class ClothingSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'clothes',
            'category',
            'price',
            'color',
            'quantity',
            'size',
            'imageurl',
            'status',
            'date_created',
        )
        model = Clothing




