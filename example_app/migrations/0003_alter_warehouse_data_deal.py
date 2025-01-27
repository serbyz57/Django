# Generated by Django 4.1.7 on 2023-04-13 11:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('example_app', '0002_warehouse_data_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='data',
            field=models.DateField(default=datetime.date(2023, 4, 13)),
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(default=datetime.date(2023, 4, 13))),
                ('amount', models.IntegerField()),
                ('price_by_one', models.IntegerField()),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example_app.product')),
            ],
        ),
    ]
