# Generated by Django 3.2.13 on 2022-05-29 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.IntegerField(blank=True, null=True)),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.IntegerField(blank=True, null=True)),
                ('fechaInicio', models.DateTimeField()),
                ('comentario', models.TextField(blank=True, max_length=280, null=True)),
                ('moduleId', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='chat.module')),
                ('personaId', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='chat.persona')),
            ],
        ),
        migrations.CreateModel(
            name='PersonModulePreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferencia', models.IntegerField(blank=True, null=True)),
                ('moduleId', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='chat.module')),
                ('personaId', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='chat.persona')),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='personaId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='chat.persona'),
        ),
    ]
