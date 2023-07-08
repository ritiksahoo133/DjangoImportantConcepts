# Generated by Django 4.1.2 on 2023-05-24 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('city', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('marks', models.IntegerField()),
            ],
        ),
    ]
