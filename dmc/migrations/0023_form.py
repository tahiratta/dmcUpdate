# Generated by Django 2.0.2 on 2018-04-03 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmc', '0022_auto_20180403_0357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('form', models.FileField(upload_to='')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'forms',
            },
        ),
    ]
