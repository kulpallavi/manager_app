# Generated by Django 3.2.5 on 2021-07-11 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_usersubscription_plan_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubscription',
            name='user_full_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
