# Generated by Django 3.1.6 on 2021-05-20 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_auto_20210520_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='owner',
        ),
    ]
