from django.db import models

class SalesData(models.Model):
       order_id = models.CharField(max_length=50, unique=True)
       order_item_id = models.CharField(max_length=50)
       quantity_ordered = models.IntegerField()
       item_price = models.FloatField()
       promotion_discount = models.FloatField()
       total_sales = models.FloatField()
       region = models.CharField(max_length=1)
       net_sales = models.FloatField()
    


