# Generated by Django 5.1.1 on 2024-09-20 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0011_alter_vehicles_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicles',
            old_name='order_time',
            new_name='time_created',
        ),
        migrations.RemoveField(
            model_name='vehicles',
            name='new',
        ),
        migrations.AddField(
            model_name='vehicles',
            name='new_old',
            field=models.CharField(choices=[('new', 'new'), ('old', 'old')], default='new', max_length=30),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
