# Generated by Django 4.2.1 on 2023-08-17 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0010_alter_profile_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default=None, null=True),
        ),
    ]
