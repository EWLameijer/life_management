# Generated by Django 2.2.2 on 2019-07-23 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20190719_0521'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmoment',
            name='remarks',
            field=models.TextField(blank=True),
        ),
    ]
