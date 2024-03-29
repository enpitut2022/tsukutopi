# Generated by Django 3.2 on 2023-01-06 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('key_number', models.IntegerField(max_length=9, primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=50)),
                ('major_sub', models.CharField(max_length=50)),
                ('circle', models.CharField(max_length=50)),
                ('hometown', models.CharField(max_length=50)),
                ('music', models.CharField(max_length=50)),
                ('ramen', models.CharField(max_length=50)),
                ('game', models.CharField(max_length=50)),
                ('anime', models.CharField(max_length=50)),
                ('movie', models.CharField(max_length=50)),
                ('sport', models.CharField(max_length=50)),
            ],
        ),
    ]
