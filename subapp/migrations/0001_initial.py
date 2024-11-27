# Generated by Django 5.1.3 on 2024-11-27 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalesData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=50, unique=True)),
                ('order_item_id', models.CharField(max_length=50)),
                ('quantity_ordered', models.IntegerField()),
                ('item_price', models.FloatField()),
                ('promotion_discount', models.FloatField()),
                ('total_sales', models.FloatField()),
                ('region', models.CharField(max_length=1)),
                ('net_sales', models.FloatField()),
            ],
        ),
    ]
