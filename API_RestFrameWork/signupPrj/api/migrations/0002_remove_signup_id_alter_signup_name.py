# Generated by Django 4.1.2 on 2022-11-17 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='id',
        ),
        migrations.AlterField(
            model_name='signup',
            name='name',
            field=models.CharField(max_length=70, primary_key=True, serialize=False),
        ),
    ]