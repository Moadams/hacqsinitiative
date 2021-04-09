# Generated by Django 3.1.5 on 2021-04-08 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20210212_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executive',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='executive',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='executive',
            name='image',
            field=models.ImageField(default='user-image', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='executive',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='executive',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
    ]