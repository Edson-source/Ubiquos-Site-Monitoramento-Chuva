# Generated by Django 4.1.8 on 2023-05-11 18:36

import core.models.firmware
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac', models.CharField(max_length=12, verbose_name='MAC')),
                ('last_call', models.DateTimeField(verbose_name='Última chamada')),
                ('latitude', models.FloatField(verbose_name='Latitude')),
                ('longitude', models.FloatField(verbose_name='Longitude')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('address', models.CharField(max_length=100, verbose_name='Endereço')),
                ('latitude', models.FloatField(verbose_name='Latitude')),
                ('longitude', models.FloatField(verbose_name='Longitude')),
            ],
        ),
        migrations.CreateModel(
            name='TempURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=400)),
                ('slug', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('valid', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Firmware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=core.models.firmware.upload_to, verbose_name='Arquivo')),
                ('version', models.IntegerField(verbose_name='Versão')),
                ('detail', models.TextField(default='', verbose_name='Detalhes da versão')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.devicemodel', verbose_name='Modelo')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.device', verbose_name='Dispositivo')),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.location', verbose_name='Local'),
        ),
        migrations.AddField(
            model_name='device',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.devicemodel', verbose_name='Modelo'),
        ),
        migrations.CreateModel(
            name='DataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome do dado')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('reference_tag', models.CharField(max_length=30, verbose_name='Tag de referência')),
                ('alert_per_time', models.TimeField(blank=True, null=True, verbose_name='Alerta por período (vazio para alerta por valor)')),
                ('warning_alert', models.FloatField(verbose_name='Valor mínimo para "Alerta"')),
                ('danger_alert', models.FloatField(verbose_name='Valor mínimo para "Perigo"')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.devicemodel', verbose_name='Modelo')),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, null=True, verbose_name='Valor')),
                ('log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datalog_set', to='core.devicelog', verbose_name='Log')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.datamodel', verbose_name='Modelo')),
            ],
        ),
    ]