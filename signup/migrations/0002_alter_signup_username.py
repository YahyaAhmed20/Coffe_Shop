# Generated by Django 5.0.1 on 2024-01-18 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]