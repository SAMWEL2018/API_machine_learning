# Generated by Django 3.2.10 on 2022-02-07 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_comments_is_positive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='is_positive',
            field=models.BooleanField(),
        ),
        migrations.AlterModelTable(
            name='comments',
            table='chats',
        ),
    ]
