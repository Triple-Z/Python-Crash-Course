# Generated by Django 2.0.2 on 2018-02-04 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
