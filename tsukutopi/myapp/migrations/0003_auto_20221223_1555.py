# Generated by Django 3.2 on 2022-12-23 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20221221_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='anime',
            field=models.IntegerField(max_length=2),
        ),
        migrations.AlterField(
            model_name='profile',
            name='game',
            field=models.IntegerField(max_length=2),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hometown',
            field=models.IntegerField(max_length=2),
        ),
        migrations.AlterField(
            model_name='profile',
            name='major_sub',
            field=models.IntegerField(max_length=2),
        ),
        migrations.AlterField(
            model_name='profile',
            name='movie',
            field=models.IntegerField(max_length=2),
        ),
        migrations.AlterField(
            model_name='profile',
            name='music',
            field=models.IntegerField(max_length=2),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ramen',
            field=models.IntegerField(max_length=2),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sport',
            field=models.IntegerField(max_length=2),
        ),
    ]
