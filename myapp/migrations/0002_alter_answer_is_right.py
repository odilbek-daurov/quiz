# Generated by Django 4.0.2 on 2022-02-11 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='is_right',
            field=models.BooleanField(default=False),
        ),
    ]
