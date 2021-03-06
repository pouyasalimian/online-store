# Generated by Django 3.2.2 on 2021-06-13 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='SlidBar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('image', models.ImageField(upload_to='slidbar/', verbose_name='image')),
                ('is_active', models.BooleanField(verbose_name='show on website')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 's',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, upload_to='', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.FloatField(verbose_name='discount'),
        ),
        migrations.AlterField(
            model_name='product',
            name='number',
            field=models.IntegerField(verbose_name='number'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='special_discount',
            field=models.FloatField(verbose_name='special_discount'),
        ),
        migrations.AlterField(
            model_name='product',
            name='special_discount_time',
            field=models.DateTimeField(auto_now=True, verbose_name='special_discount_time'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='slidbar',
            name='product',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
