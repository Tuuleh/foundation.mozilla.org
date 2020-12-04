# Generated by Django 2.2.16 on 2020-12-04 01:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0022_product_voting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpage',
            name='review_date',
            field=models.DateField(default=django.utils.timezone.now, help_text='Review date of this product'),
        ),
    ]