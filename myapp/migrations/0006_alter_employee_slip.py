# Generated by Django 4.1.5 on 2023-04-18 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_employee_proj_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='slip',
            field=models.CharField(max_length=1000),
        ),
    ]
