# Generated by Django 2.2.5 on 2020-01-15 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='discription',
            field=models.TextField(),
        ),
    ]