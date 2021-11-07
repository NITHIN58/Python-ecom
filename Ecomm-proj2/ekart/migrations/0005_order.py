# Generated by Django 3.2.6 on 2021-09-20 08:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
        ('ekart', '0004_auto_20210914_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(null=True)),
                ('order_total', models.IntegerField(null=True)),
                ('payment_method', models.CharField(default='', max_length=50, null=True)),
                ('delivery_date', models.DateField(null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Accepted', 'Accepted'), ('Out for Delivery', 'Out for Delivery'), ('Order Cancel', 'Order Cancel'), ('Customer Cancel', 'Customer Cancel'), ('Delivered', 'Delivered'), ('Added to Cart', 'Added to Cart'), ('Assigned to Driver', 'Assigned to Driver')], default='ordered', max_length=50, null=True)),
                ('Is_deliverd', models.BooleanField(default=False)),
                ('customer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vendor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor')),
            ],
        ),
    ]
