# Generated by Django 3.1.4 on 2020-12-02 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20201202_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Categories', to='store.categories'),
        ),
    ]
