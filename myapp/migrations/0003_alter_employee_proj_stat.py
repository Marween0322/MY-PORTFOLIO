# Generated by Django 4.1.5 on 2023-04-13 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_employee_cont_alter_employee_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='proj_stat',
            field=models.CharField(choices=[('Complate', 'Complete'), ('On-Going', 'On-Going'), ('Under Procurement', 'Under Procurement')], max_length=20, null=True),
        ),
    ]
