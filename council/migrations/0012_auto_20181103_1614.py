# Generated by Django 2.1.1 on 2018-11-03 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('council', '0011_auto_20181029_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
    ]
