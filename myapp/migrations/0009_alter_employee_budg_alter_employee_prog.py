# Generated by Django 4.1.5 on 2023-04-19 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_employee_progress_employee_prog_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='budg',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='progress',
            field=models.IntegerField(null=True),
        ),
    ]
