# Generated by Django 4.1.3 on 2022-11-12 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='account_type',
            field=models.CharField(blank=True, choices=[('Driver', 'Driver'), ('Parent', 'Parent')], max_length=30, null=True),
        ),
    ]
