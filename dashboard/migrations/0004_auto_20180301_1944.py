# Generated by Django 2.0.1 on 2018-03-01 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20180227_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='requested_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
