# Generated by Django 3.1.4 on 2020-12-08 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0002_purchases_isactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchases',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]
