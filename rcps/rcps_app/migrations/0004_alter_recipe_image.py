# Generated by Django 4.1.6 on 2023-02-18 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rcps_app', '0003_recipe_created_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
