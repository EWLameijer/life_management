# Generated by Django 2.2.2 on 2019-07-19 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20190718_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='contacts.Person'),
        ),
    ]