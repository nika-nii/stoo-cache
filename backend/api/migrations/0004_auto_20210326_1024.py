# Generated by Django 3.1.4 on 2021-03-26 07:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_review_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 3, 26, 10, 24, 7, 196838)),
        ),
    ]
