# Generated by Django 4.1.3 on 2024-06-11 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0006_rename_cart_carts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(default=False, max_length=50),
        ),
    ]