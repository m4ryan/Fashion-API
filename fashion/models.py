from django.db import models

# Create your models here.
from django.db import models

class Merchant(models.Model):
    merchant_id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    rating = models.FloatField()
    rating_count = models.IntegerField()

    def __str__(self):
        return self.name

class FashionProduct(models.Model):
    product_id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=255)
    price = models.FloatField()
    retail_price = models.FloatField()
    currency = models.CharField(max_length=10)
    units_sold = models.IntegerField()
    rating = models.FloatField()
    rating_count = models.IntegerField()
    color = models.CharField(max_length=50, null=True, blank=True)
    size = models.CharField(max_length=50, null=True, blank=True)
    tags = models.TextField(null=True, blank=True)
    theme = models.CharField(max_length=20)
    crawl_month = models.CharField(max_length=10)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
