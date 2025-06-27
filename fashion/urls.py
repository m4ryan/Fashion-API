from django.urls import path
from .views import (
    FashionProductListView,
    FashionProductCreateView,
    ProductByColorView,
    HighRatedProductsView,
    MerchantListView,
    ProductsByMerchantView,
    api_home,
)

urlpatterns = [
    path('', api_home, name='api-home'),  # 👈 this is the missing line
    path('products/', FashionProductListView.as_view(), name='all-products'),
    path('products/create/', FashionProductCreateView.as_view(), name='create-product'),
    path('products/color/<str:color>/', ProductByColorView.as_view(), name='products-by-color'),
    path('products/high-rated/', HighRatedProductsView.as_view(), name='high-rated-products'),
    path('merchants/', MerchantListView.as_view(), name='all-merchants'),
    path('merchants/<str:merchant_id>/products/', ProductsByMerchantView.as_view(), name='merchant-products'),
]
