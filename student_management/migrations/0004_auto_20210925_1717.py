# Generated by Django 3.2.7 on 2021-09-25 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0003_enrolledcourse_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolledcourse',
            name='grade',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='student',
            name='gpa',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]