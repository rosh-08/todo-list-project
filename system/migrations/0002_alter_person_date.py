# Generated by Django 4.0.4 on 2022-07-17 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date',
            field=models.DateField(null='True'),
        ),
    ]