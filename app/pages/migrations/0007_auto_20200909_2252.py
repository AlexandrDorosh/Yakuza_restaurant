# Generated by Django 3.1.1 on 2020-09-09 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20200909_2251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dessert',
            options={'verbose_name': 'Dessert', 'verbose_name_plural': 'Dessert'},
        ),
        migrations.AlterModelOptions(
            name='sushi',
            options={'verbose_name': 'Sushi', 'verbose_name_plural': 'Sushi'},
        ),
    ]
