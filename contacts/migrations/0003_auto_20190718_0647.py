# Generated by Django 2.2.2 on 2019-07-18 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20190717_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectiontype',
            name='description',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Person', unique=True),
        ),
        migrations.AlterField(
            model_name='contacttype',
            name='description',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='connection',
            unique_together={('subject', 'other_person')},
        ),
        migrations.AlterUniqueTogether(
            name='contactmoment',
            unique_together={('name', 'date')},
        ),
    ]
