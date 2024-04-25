from .views import productsPageView, productPageView
from django.urls import path

urlpatterns = [
    path('', productsPageView, name='products'),
    path('product', productPageView, name='product'),
]