# Generated by Django 5.0.4 on 2024-04-17 23:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Casas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=255)),
                ('numerohabitaciones', models.CharField(max_length=255)),
                ('añocontruccion', models.CharField(max_length=255)),
                ('tipocontruccion', models.CharField(choices=[('tradicional', 'Tradicional'), ('moderno', 'Moderno'), ('otros', 'Otros')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Edificios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=255)),
                ('tipoedificio', models.CharField(choices=[('residencial', 'Residencial'), ('comercial', 'Comercial'), ('oficinas', 'Oficinas'), ('otros', 'Otros')], max_length=255)),
                ('estadoedificio', models.CharField(max_length=255)),
                ('añoconstruccion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Fincas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=255)),
                ('tamañoterreno', models.CharField(max_length=255)),
                ('actividad', models.CharField(choices=[('agricultura', 'Agricultura'), ('ganaderia', 'Ganadería'), ('forestal', 'Forestal'), ('otros', 'Otros')], max_length=255)),
                ('infraestructura', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Propietarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('celular', models.CharField(max_length=255)),
                ('cedula', models.CharField(max_length=255)),
                ('idcasas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propietarios_casas_list', to='inmobiliaria_app.casas')),
                ('idedificios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propietarios_edificios_list', to='inmobiliaria_app.edificios')),
                ('idfincas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propietarios_fincas_list', to='inmobiliaria_app.fincas')),
            ],
        ),
    ]
