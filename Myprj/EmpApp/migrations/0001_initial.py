# Generated by Django 4.0.5 on 2022-06-24 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ename', models.CharField(max_length=20)),
                ('salary', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Emp',
            },
        ),
    ]
