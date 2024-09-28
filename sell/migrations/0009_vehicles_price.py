# Generated by Django 5.1.1 on 2024-09-15 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0008_alter_vehicles_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicles',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
