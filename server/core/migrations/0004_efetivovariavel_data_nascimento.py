# Generated by Django 4.1.7 on 2023-04-09 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_efetivovariavel_foto_alter_fatd_data_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='efetivovariavel',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
    ]