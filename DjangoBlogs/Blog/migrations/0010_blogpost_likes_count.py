# Generated by Django 4.2.1 on 2023-08-15 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0009_alter_like_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='likes_count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
