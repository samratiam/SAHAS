# Generated by Django 4.1.3 on 2022-11-12 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_location_user_phone_alter_user_account_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fullname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
