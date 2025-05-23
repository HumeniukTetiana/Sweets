# Generated by Django 5.1.5 on 2025-04-29 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fullorder',
            name='points_used',
        ),
        migrations.RemoveField(
            model_name='person',
            name='phone',
        ),
        migrations.AddField(
            model_name='person',
            name='_phone',
            field=models.CharField(blank=True, db_column='phone', max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
