# Generated by Django 4.1.2 on 2023-05-17 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_alter_student_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(),
        ),
    ]
