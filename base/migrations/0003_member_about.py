# Generated by Django 3.1.5 on 2021-01-08 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20210107_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
    ]
