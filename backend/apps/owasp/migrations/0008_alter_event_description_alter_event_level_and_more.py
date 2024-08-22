# Generated by Django 5.1 on 2024-08-22 22:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("owasp", "0007_event"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="description",
            field=models.CharField(
                blank=True, default="", max_length=500, verbose_name="Description"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="level",
            field=models.CharField(blank=True, default="", max_length=5, verbose_name="Level"),
        ),
        migrations.AlterField(
            model_name="event",
            name="tags",
            field=models.JSONField(blank=True, default=list, verbose_name="Tags"),
        ),
        migrations.AlterField(
            model_name="event",
            name="url",
            field=models.URLField(blank=True, default="", verbose_name="URL"),
        ),
    ]
