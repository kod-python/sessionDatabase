# Generated by Django 4.1.3 on 2024-06-12 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0008_rename_cartitem_orderitem_alter_order_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(default='Credit-Card/Debit-Card', max_length=50),
        ),
    ]