# Generated by Django 3.0.5 on 2020-04-08 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facts', '0005_auto_20200408_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
