# Generated by Django 3.2 on 2023-02-21 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signage', '0004_auto_20230219_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('has_consulting_rooms_changed', models.BooleanField(default=False)),
                ('has_operating_rooms_changed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'DataTracker',
                'verbose_name_plural': 'DataTracker',
            },
        ),
    ]
