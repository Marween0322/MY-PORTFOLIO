# Generated by Django 4.1.5 on 2023-04-05 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc', models.CharField(max_length=1000)),
                ('desc', models.CharField(max_length=1000)),
                ('fund', models.CharField(max_length=1000)),
                ('cont', models.CharField(max_length=1000)),
                ('proj_profile', models.CharField(max_length=1000)),
                ('proj_stat', models.CharField(max_length=1000)),
                ('slip', models.CharField(max_length=1000)),
                ('budg', models.CharField(max_length=1000)),
                ('agency', models.CharField(max_length=1000)),
                ('area', models.CharField(max_length=1000)),
                ('reg', models.CharField(max_length=1000)),
                ('cert', models.CharField(max_length=1000)),
                ('reco', models.CharField(max_length=1000)),
                ('progress', models.IntegerField()),
                


                
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
