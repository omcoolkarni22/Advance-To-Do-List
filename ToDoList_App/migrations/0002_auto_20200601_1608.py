# Generated by Django 3.0 on 2020-06-01 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoList_App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='username',
            new_name='email',
        ),
        migrations.AlterField(
            model_name='tasks',
            name='is_InProgress',
            field=models.BooleanField(default=False),
        ),
    ]
