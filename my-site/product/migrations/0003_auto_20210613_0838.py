# Generated by Django 3.2.2 on 2021-06-13 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210613_0827'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slidbar',
            options={'verbose_name': 'slider', 'verbose_name_plural': 'sliders'},
        ),
        migrations.RemoveField(
            model_name='slidbar',
            name='product',
        ),
    ]