# Generated by Django 4.1.2 on 2023-05-24 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('s_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.student')),
            ],
        ),
    ]
