# Generated by Django 3.1.5 on 2021-02-13 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20210210_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]