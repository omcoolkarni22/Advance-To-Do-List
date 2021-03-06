# Generated by Django 3.0 on 2020-06-01 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='username', max_length=50)),
                ('start_date', models.CharField(default='start date and time', max_length=50)),
                ('end_date', models.CharField(default=' end date and time', max_length=50)),
                ('is_archive', models.BooleanField(default=False)),
                ('is_completed', models.BooleanField(default=False)),
                ('is_InProgress', models.BooleanField(default=True)),
                ('Task', models.TextField()),
            ],
        ),
    ]
