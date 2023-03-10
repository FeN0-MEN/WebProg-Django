# Generated by Django 4.1.1 on 2022-10-03 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_alter_book_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(default='', max_length=255)),
                ('password', models.CharField(default='', max_length=128)),
                ('email', models.CharField(default='', max_length=255)),
                ('handle', models.CharField(default='', max_length=255)),
                ('role', models.CharField(default='', max_length=255)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
