# Generated by Django 5.0.6 on 2024-05-26 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food_item", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="item_image",
            field=models.CharField(
                default="https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg",
                max_length=500,
            ),
        ),
    ]
