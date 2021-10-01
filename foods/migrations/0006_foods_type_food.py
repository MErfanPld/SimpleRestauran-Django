# Generated by Django 3.2.6 on 2021-08-29 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0005_remove_foods_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='foods',
            name='type_food',
            field=models.CharField(choices=[('A', 'All'), ('D', 'Drinks'), ('L', 'Lunch'), ('DI', 'Dinner')], default='A', max_length=50),
        ),
    ]