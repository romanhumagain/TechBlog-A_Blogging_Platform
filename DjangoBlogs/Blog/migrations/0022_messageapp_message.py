# Generated by Django 4.2.1 on 2023-09-06 07:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0021_rename_message_messageapp'),
    ]

    operations = [
        migrations.AddField(
            model_name='messageapp',
            name='message',
            field=models.CharField(default=datetime.datetime(2023, 9, 6, 7, 3, 17, 803376, tzinfo=datetime.timezone.utc), max_length=100),
            preserve_default=False,
        ),
    ]
