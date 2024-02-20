# Generated by Django 4.2.10 on 2024-02-20 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("watchlist_app", "0006_alter_review_reviewer"),
    ]

    operations = [
        migrations.AddField(
            model_name="watchlist",
            name="avg_rating",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="watchlist",
            name="number_of_ratings",
            field=models.IntegerField(default=0),
        ),
    ]