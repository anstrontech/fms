# Generated by Django 3.1.3 on 2020-11-03 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=100)),
                ('enrollNo', models.CharField(max_length=100)),
                ('fullName', models.CharField(max_length=100)),
                ('emailID', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('semester', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
            ],
        ),
    ]