# Generated by Django 2.0.2 on 2018-04-02 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmc', '0009_auto_20180402_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='message',
            field=models.TextField(blank=True, max_length=2000),
        ),
    ]
