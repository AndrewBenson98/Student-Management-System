# Generated by Django 3.2.7 on 2021-09-25 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0002_course_enrolledcourse'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrolledcourse',
            name='grade',
            field=models.DecimalField(decimal_places=2, default=75.0, max_digits=5),
        ),
    ]
