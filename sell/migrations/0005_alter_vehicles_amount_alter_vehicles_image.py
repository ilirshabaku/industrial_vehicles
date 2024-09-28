# Generated by Django 5.1.1 on 2024-09-14 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0004_rename_uuid_vehicles_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicles',
            name='amount',
            field=models.CharField(choices=[('one', 'one'), ('two', 'two'), ('three', 'three'), ('four', 'four')], default='one', max_length=300000),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
