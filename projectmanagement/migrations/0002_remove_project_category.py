# Generated by Django 3.2.16 on 2023-03-25 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanagement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='category',
        ),
    ]