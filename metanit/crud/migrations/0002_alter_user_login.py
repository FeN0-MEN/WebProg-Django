# Generated by Django 4.1.1 on 2022-11-06 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
    ]
