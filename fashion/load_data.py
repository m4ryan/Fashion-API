import pandas as pd
from fashion.models import FashionProduct, Merchant
from django.db import transaction

def run():
    df = pd.read_csv('summer-products.csv')

    with transaction.atomic():
        for _, row in df.iterrows():
            merchant, _ = Merchant.objects.get_or_create(
                merchant_id=row['merchant_id'],
                defaults={
                    'name': row.get('merchant_name', '') or 'Unknown',
                    'title': row.get('merchant_title', '') or 'Untitled',
                    'rating': row.get('merchant_rating', 0.0),
                    'rating_count': row.get('merchant_rating_count', 0),
                }
            )

            FashionProduct.objects.update_or_create(
                product_id=row['product_id'],
                defaults={
                    'title': row['title'],
                    'price': row['price'],
                    'retail_price': row['retail_price'],
                    'currency': row['currency_buyer'],
                    'units_sold': row['units_sold'],
                    'rating': row['rating'],
                    'rating_count': row['rating_count'],
                    'color': row.get('product_color'),
                    'size': row.get('product_variation_size_id'),
                    'tags': row.get('tags'),
                    'theme': row.get('theme', 'summer'),
                    'crawl_month': row.get('crawl_month', ''),
                    'merchant': merchant,
                }
            )
