# Generated by Django 3.0.3 on 2020-02-06 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facts', '0002_auto_20200206_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='fact',
            name='author',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
