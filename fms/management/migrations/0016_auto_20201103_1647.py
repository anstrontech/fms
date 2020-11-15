# Generated by Django 3.1.3 on 2020-11-03 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0015_auto_20201103_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty_subject',
            name='subjectID',
        ),
        migrations.AlterField(
            model_name='faculty_subject',
            name='faculty',
            field=models.CharField(choices=[('USER18313', 'Test Faculty')], default=None, max_length=100),
        ),
    ]