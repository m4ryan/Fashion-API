from django.shortcuts import render

# Create your views here.
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FashionProduct, Merchant
from .serializers import FashionProductSerializer, MerchantSerializer

# 1. List all products
class FashionProductListView(generics.ListAPIView):
    queryset = FashionProduct.objects.all()
    serializer_class = FashionProductSerializer

# 2. Create a new product
class FashionProductCreateView(generics.CreateAPIView):
    queryset = FashionProduct.objects.all()
    serializer_class = FashionProductSerializer

# 3. List products by color
class ProductByColorView(generics.ListAPIView):
    serializer_class = FashionProductSerializer

    def get_queryset(self):
        color = self.kwargs['color']
        return FashionProduct.objects.filter(color__iexact=color)

# 4. List products with rating above 4
class HighRatedProductsView(generics.ListAPIView):
    serializer_class = FashionProductSerializer
    queryset = FashionProduct.objects.filter(rating__gte=4.0)

# 5. List all merchants
class MerchantListView(generics.ListAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

# 6. Products by merchant ID
class ProductsByMerchantView(generics.ListAPIView):
    serializer_class = FashionProductSerializer

    def get_queryset(self):
        merchant_id = self.kwargs['merchant_id']
        return FashionProduct.objects.filter(merchant__merchant_id=merchant_id)
import django
import sys
import pkg_resources
from django.http import JsonResponse
from django.urls import reverse

def api_home(request):
    packages = {dist.key: dist.version for dist in pkg_resources.working_set}
    return JsonResponse({
        "message": "Welcome to the Fashion API",
        "python_version": sys.version,
        "django_version": django.get_version(),
        "admin_site": "/admin/ (username: admin, password: admin123)",  # customize as needed
        "endpoints": {
            "all_products": reverse('all-products'),
            "create_product": reverse('create-product'),
            "products_by_color": "/api/products/color/<color>/",
            "high_rated_products": reverse('high-rated-products'),
            "all_merchants": reverse('all-merchants'),
            "products_by_merchant": "/api/merchants/<merchant_id>/products/",
        },
        "installed_packages": packages,
    }, json_dumps_params={"indent": 2})
