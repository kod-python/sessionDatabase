# Generated by Django 4.1.3 on 2024-06-20 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0023_orderitem_product_orderitem_total_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='company_name',
            field=models.CharField(blank=True, default='company_name', max_length=100, null=True),
        ),
    ]