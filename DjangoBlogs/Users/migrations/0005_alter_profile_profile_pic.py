# Generated by Django 4.2.1 on 2023-08-12 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_alter_profile_bio_alter_profile_follower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics'),
        ),
    ]