# Generated by Django 4.2.5 on 2023-09-28 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(max_length=50),
        ),
    ]