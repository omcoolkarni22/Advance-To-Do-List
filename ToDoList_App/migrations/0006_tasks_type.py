# Generated by Django 3.0 on 2020-06-03 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoList_App', '0005_remove_tasks_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='type',
            field=models.CharField(default=' Personal', max_length=50),
        ),
    ]