# Generated by Django 3.1.2 on 2020-11-02 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_data_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='name',
        ),
    ]
