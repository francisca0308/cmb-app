# Generated by Django 3.2.13 on 2022-05-29 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_module_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]
