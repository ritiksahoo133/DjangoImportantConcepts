# Generated by Django 3.1.7 on 2021-08-31 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=10)),
                ('price', models.FloatField(default=100)),
                ('brand', models.CharField(max_length=10)),
                ('quantity', models.IntegerField()),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]
