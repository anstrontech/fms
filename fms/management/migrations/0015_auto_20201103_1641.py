# Generated by Django 3.1.3 on 2020-11-03 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0014_auto_20201103_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty_subject',
            name='faculty',
            field=models.CharField(choices=[], default=None, max_length=100),
        ),
    ]
