# Generated by Django 4.1.3 on 2023-03-19 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_phone_profile_agentname'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='id_user',
            field=models.CharField(default=1, max_length=100000000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='houseuploads',
            name='user',
            field=models.TextField(max_length=100),
        ),
    ]
