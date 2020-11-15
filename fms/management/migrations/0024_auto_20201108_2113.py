# Generated by Django 3.1.3 on 2020-11-08 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0023_auto_20201108_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty_subject',
            name='course',
            field=models.CharField(choices=[('MCA3663', 'MCA'), ('BCA9610', 'BCA'), ('BBA4615', 'BBA'), ('MBA8269', 'MBA')], default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='faculty_subject',
            name='faculty',
            field=models.CharField(choices=[('USER18313', 'Test Faculty'), ('USER32093', 'Hardik Soni'), ('USER26264', 'Test Faculty 1')], default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='feedback_reply',
            name='courseid',
            field=models.CharField(choices=[('MCA3663', 'MCA'), ('BCA9610', 'BCA'), ('BBA4615', 'BBA'), ('MBA8269', 'MBA')], max_length=10),
        ),
        migrations.AlterField(
            model_name='feedback_reply',
            name='facultyid',
            field=models.CharField(choices=[('USER18313', 'Test Faculty'), ('USER32093', 'Hardik Soni'), ('USER26264', 'Test Faculty 1')], max_length=10),
        ),
        migrations.AlterField(
            model_name='feedback_reply',
            name='questionid',
            field=models.CharField(blank=True, choices=[('QUS11036', 'how is practical goes'), ('QUS47444', 'how is practical goes sd'), ('QUS70627', 'how is practical goes dsgfsfg')], max_length=10),
        ),
        migrations.AlterField(
            model_name='feedback_reply',
            name='semester',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=10),
        ),
        migrations.AlterField(
            model_name='feedback_reply',
            name='studentid',
            field=models.CharField(choices=[('USER85388', 'Tirth Jain'), ('USER25335', 'Henil Shah')], max_length=10),
        ),
        migrations.AlterField(
            model_name='feedback_reply',
            name='subjectid',
            field=models.CharField(choices=[('SUB8463', 'ML'), ('SUB3964', 'DAA'), ('SUB8301', 'Software Engineering'), ('SUB3177', 'Laravel'), ('SUB1669', 'test')], max_length=10),
        ),
    ]
