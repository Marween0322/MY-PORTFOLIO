# Generated by Django 4.1.5 on 2023-04-19 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_employee_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='progress',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
