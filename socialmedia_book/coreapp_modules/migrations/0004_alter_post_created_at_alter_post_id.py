# Generated by Django 4.1.3 on 2022-12-16 11:26

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp_modules', '0003_alter_post_created_at_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 11, 26, 4, 628069)),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b9d6c1b8-aee5-42c2-a1ac-f5989378fba8'), primary_key=True, serialize=False),
        ),
    ]
