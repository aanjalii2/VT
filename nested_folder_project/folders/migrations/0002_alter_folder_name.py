# Generated by Django 5.0.3 on 2024-07-07 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]