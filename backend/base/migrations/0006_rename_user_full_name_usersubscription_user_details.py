# Generated by Django 3.2.5 on 2021-07-11 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_usersubscription_user_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersubscription',
            old_name='user_full_name',
            new_name='user_details',
        ),
    ]
