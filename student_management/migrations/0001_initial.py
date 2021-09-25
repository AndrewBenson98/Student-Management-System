# Generated by Django 3.2.7 on 2021-09-25 19:15

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
                ('studentID', models.CharField(max_length=9, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phoneNumber', models.CharField(blank=True, max_length=15)),
                ('gpa', models.DecimalField(decimal_places=2, default=3.0, max_digits=3)),
            ],
        ),
    ]
