# Generated by Django 3.2.5 on 2021-07-18 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_remove_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
