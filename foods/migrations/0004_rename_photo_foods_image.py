# Generated by Django 3.2.6 on 2021-08-29 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0003_remove_foods_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foods',
            old_name='photo',
            new_name='image',
        ),
    ]
