# Generated by Django 3.2 on 2022-04-10 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aromaticblog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]
