# Generated by Django 4.0.4 on 2022-07-18 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_person_sr_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date',
            field=models.DateField(),
        ),
    ]
