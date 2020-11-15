# Generated by Django 3.1.3 on 2020-11-04 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0016_auto_20201103_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty_subject',
            name='subjectName',
            field=models.CharField(choices=[('SUB8463', 'ML'), ('SUB3964', 'DAA'), ('SUB8301', 'Software Engineering')], default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='course',
            field=models.CharField(blank=True, choices=[('MCA3663', 'MCA'), ('BCA9610', 'BCA'), ('BBA4615', 'BBA'), ('MBA8269', 'MBA')], max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='semester',
            field=models.CharField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], max_length=100),
        ),
    ]
