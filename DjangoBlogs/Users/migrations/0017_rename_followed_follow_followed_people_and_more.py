# Generated by Django 4.2.1 on 2023-09-07 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0016_rename_follower_follow_followers_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='followed',
            new_name='followed_people',
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('followers', 'followed_people')},
        ),
    ]