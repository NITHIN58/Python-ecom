# Generated by Django 3.2.6 on 2021-10-07 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ekart', '0007_addtocart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addtocart',
            old_name='aproduct',
            new_name='cartproduct',
        ),
        migrations.RenameField(
            model_name='addtocart',
            old_name='quantity',
            new_name='cartquantity',
        ),
        migrations.RenameField(
            model_name='addtocart',
            old_name='auser',
            new_name='cartuser',
        ),
    ]
