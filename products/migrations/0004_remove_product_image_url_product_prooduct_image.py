# Generated by Django 5.0.2 on 2024-02-28 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.AddField(
            model_name='product',
            name='prooduct_image',
            field=models.FileField(null=True, upload_to='static/uploads'),
        ),
    ]
