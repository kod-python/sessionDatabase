# Generated by Django 4.1.3 on 2024-06-11 13:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Product', '0003_cart'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart',
            new_name='Carts',
        ),
    ]
