# Generated by Django 4.1.3 on 2024-06-11 15:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Product', '0005_cart_cartitem_remove_orderitem_order_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart',
            new_name='Carts',
        ),
    ]