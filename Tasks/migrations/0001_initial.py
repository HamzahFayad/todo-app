# Generated by Django 3.0.8 on 2020-07-26 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_photo', models.ImageField(blank=True, null=True, upload_to='task_photos/')),
                ('text', models.CharField(max_length=200)),
                ('date_published', models.DateTimeField(blank=True, default=datetime.date.today)),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'ordering': ['date_published'],
            },
        ),
    ]
