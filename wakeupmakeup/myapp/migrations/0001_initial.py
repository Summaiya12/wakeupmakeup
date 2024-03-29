# Generated by Django 4.2.5 on 2023-09-21 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField(default='', max_length=300)),
                ('image', models.ImageField(upload_to='shop/image')),
                ('price', models.IntegerField(default='')),
                ('quantity', models.IntegerField(default='')),
                ('category', models.CharField(choices=[('1', 'brush'), ('2', 'lipstick'), ('3', 'powder'), ('4', 'foundation'), ('5', 'tint'), ('6', 'shadow'), ('7', 'liner'), ('8', 'blush'), ('9', 'mascara'), ('10', 'perfume'), ('11', 'nail'), ('12', 'hair')], max_length=2)),
            ],
        ),
    ]
