# Generated by Django 4.2.11 on 2024-03-18 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basicchallenge',
            name='challenge_score',
        ),
    ]
