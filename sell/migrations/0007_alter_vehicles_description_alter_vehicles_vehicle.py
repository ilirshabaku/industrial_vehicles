# Generated by Django 5.1.1 on 2024-09-14 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0006_alter_vehicles_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicles',
            name='description',
            field=models.TextField(blank=True, max_length=180, null=True),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='vehicle',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]