

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=200)),
                ('image', models.ImageField(default='default.jpg', upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=11)),
                ('image', models.ImageField(default='default.jpg', upload_to='pics')),
                ('categories_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.categories')),
            ],
        ),
    ]
