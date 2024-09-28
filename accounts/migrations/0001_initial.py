# Generated by Django 5.1.1 on 2024-09-21 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=30)),
            ],
        ),
    ]
