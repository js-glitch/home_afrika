# Generated by Django 3.1.6 on 2021-02-13 10:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20210213_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
    ]
