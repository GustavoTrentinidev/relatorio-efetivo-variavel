# Generated by Django 4.1.7 on 2023-04-19 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_efetivovariavel_data_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fatd',
            name='data',
            field=models.DateField(blank=True, default='2023-04-19', null=True),
        ),
        migrations.AlterField(
            model_name='fatoobservado',
            name='data',
            field=models.DateField(blank=True, default='2023-04-19', null=True),
        ),
    ]
