# Generated by Django 2.2.2 on 2019-07-23 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_contactmoment_remarks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmoment',
            old_name='name',
            new_name='contact',
        ),
        migrations.AlterUniqueTogether(
            name='contactmoment',
            unique_together={('contact', 'date')},
        ),
    ]
