# Generated by Django 4.1.3 on 2024-06-18 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0018_remove_order_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=False, max_digits=10),
        ),
    ]
