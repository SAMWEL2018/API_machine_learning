# Generated by Django 3.2.10 on 2022-01-29 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='is_positive',
            field=models.BooleanField(default=True),
        ),
    ]
