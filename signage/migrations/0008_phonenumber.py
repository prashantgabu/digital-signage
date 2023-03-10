# Generated by Django 3.2 on 2023-02-26 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signage', '0007_auto_20230225_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phone_number', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Phone Number',
                'verbose_name_plural': 'Phone Number',
            },
        ),
    ]
