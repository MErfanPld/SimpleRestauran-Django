# Generated by Django 3.2.6 on 2021-09-02 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('little_story', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='about/')),
            ],
        ),
    ]
