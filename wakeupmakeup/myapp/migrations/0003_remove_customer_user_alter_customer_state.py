# Generated by Django 4.2.5 on 2023-09-25 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(max_length=1),
        ),
    ]
