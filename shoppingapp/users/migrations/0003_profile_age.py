# Generated by Django 3.1.4 on 2020-12-10 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
