# Generated by Django 3.1.3 on 2020-11-03 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0012_subject_semester'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subject',
            new_name='Faculty_subject',
        ),
    ]