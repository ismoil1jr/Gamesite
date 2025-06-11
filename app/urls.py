# urls.py
from django.urls import path
from app.views import HomeView, ShopView, ContactView, ProductDetailsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('product-details/<int:id>/', ProductDetailsView.as_view(), name='product_details'),
    
]




