# Generated by Django 4.0.2 on 2022-02-14 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0002_alter_customer_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='commission',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='commission',
            field=models.FloatField(default=0.04),
        ),
    ]
