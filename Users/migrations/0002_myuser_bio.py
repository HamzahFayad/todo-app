# Generated by Django 3.0.8 on 2020-08-11 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='bio',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]
