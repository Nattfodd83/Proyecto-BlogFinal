# Generated by Django 4.1.1 on 2022-10-03 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_accounts', '0002_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='red_social',
            field=models.URLField(blank=True),
        ),
    ]
