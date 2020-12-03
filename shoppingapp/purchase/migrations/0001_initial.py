# Generated by Django 3.1.4 on 2020-12-03 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0003_auto_20201202_0653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('Users_ID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Users_ID', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPurchases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=1, max_digits=3)),
                ('price', models.DecimalField(decimal_places=3, max_digits=9)),
                ('product_ID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='product_ID', to='store.product')),
                ('purchases_ID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Purchase_ID', to='purchase.purchases')),
            ],
        ),
    ]
