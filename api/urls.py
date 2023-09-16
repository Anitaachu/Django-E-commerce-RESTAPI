from django.urls import path 
from .views import CategoryView, DetailCategory, BookView, DetailBook, GroceryView, DetailGrocery, ClothingView


urlpatterns = [
    path('category/', CategoryView.as_view(), name='category'),
    path('category/<int:pk>/', DetailCategory.as_view(), name= 'singleCategory'),
    path('books', BookView.as_view(), name= 'books'),
    path('books/<int:pk>/', DetailBook.as_view(), name = 'singlebook'),
    path('grocery', GroceryView.as_view(), name='grocery'),
    path('grocery/<int:pk>/', DetailGrocery.as_view(), name = 'singleproduct'),
    path('clothes', ClothingView.as_view(), name='clothes'),
]

