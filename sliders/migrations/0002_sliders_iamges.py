# Generated by Django 3.2.6 on 2021-09-05 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sliders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sliders',
            name='iamges',
            field=models.ImageField(blank=True, upload_to='sliders/'),
        ),
    ]