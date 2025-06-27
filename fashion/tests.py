from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import FashionProduct, Merchant

class FashionAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.merchant = Merchant.objects.create(
            merchant_id="m1",
            name="Test Merchant",
            title="Vendor of Cool Stuff",
            rating=4.5,
            rating_count=123
        )

        # Create test products
        self.product1 = FashionProduct.objects.create(
            product_id="p1",
            title="Red T-Shirt",
            price=20.0,
            retail_price=25.0,
            currency="USD",
            units_sold=100,
            rating=4.5,
            rating_count=50,
            color="Red",
            size="M",
            tags="tshirt, red, summer",
            theme="Summer",
            crawl_month="June",
            merchant=self.merchant
        )

        self.product2 = FashionProduct.objects.create(
            product_id="p2",
            title="Blue Dress",
            price=50.0,
            retail_price=60.0,
            currency="USD",
            units_sold=200,
            rating=3.8,
            rating_count=70,
            color="Blue",
            size="L",
            tags="dress, party, blue",
            theme="Winter",
            crawl_month="June",
            merchant=self.merchant
        )

    def test_api_home(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Welcome to the Fashion API", response.json().get("message", ""))

    def test_get_all_products(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)

    def test_create_product(self):
        data = {
            "product_id": "p3",
            "title": "Black Watch",
            "price": 80.0,
            "retail_price": 100.0,
            "currency": "USD",
            "units_sold": 10,
            "rating": 4.9,
            "rating_count": 5,
            "color": "Black",
            "size": "One Size",
            "tags": "watch, black, formal",
            "theme": "Fall",
            "crawl_month": "June",
            "merchant": self.merchant.merchant_id
        }
        response = self.client.post('/api/products/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FashionProduct.objects.count(), 3)

    def test_get_products_by_color(self):
        response = self.client.get('/api/products/color/Red/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]["color"], "Red")

    def test_get_high_rated_products(self):
        response = self.client.get('/api/products/high-rated/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(p['rating'] >= 4.0 for p in response.json()))

    def test_get_all_merchants(self):
        response = self.client.get('/api/merchants/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_get_products_by_merchant(self):
        response = self.client.get(f'/api/merchants/{self.merchant.merchant_id}/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)
