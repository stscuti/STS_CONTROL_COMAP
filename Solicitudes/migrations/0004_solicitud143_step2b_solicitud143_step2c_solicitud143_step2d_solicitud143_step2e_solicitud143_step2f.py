# Generated by Django 2.2.9 on 2020-03-17 16:18

import Solicitudes.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Contribuyentes', '0002_auto_20200312_2105'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Solicitudes', '0003_auto_20200316_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud143_Step2f',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.BigIntegerField(blank=True, null=True)),
                ('num_expediente', models.BigIntegerField(default=Solicitudes.models.Solicitud143_Step2f.Incrementar, verbose_name='Numero de Expediente')),
                ('ind_sect_ACC', models.BooleanField(default=False, help_text='Inversiones en adaptación al cambio climático', verbose_name='Inversiones en adaptación al cambio climático')),
                ('ind_sect_DPP', models.BooleanField(default=False, help_text='Diferenciación de productos y procesos', verbose_name='Diferenciación de productos y procesos')),
                ('ind_sect_FCC', models.BooleanField(default=False, help_text='Formación continua y capacitación', verbose_name='Formación continua y capacitación')),
                ('ind_sect_ERV', models.BooleanField(default=False, help_text='Energías renovables de vanguardia', verbose_name='Energías renovables de vanguardia')),
                ('ind_sect_DMC', models.BooleanField(default=False, help_text='Desarrollo de mercado de capitales', verbose_name='Desarrollo de mercado de capitales')),
                ('contribuyente', models.ForeignKey(help_text='Contribuyente', on_delete=django.db.models.deletion.CASCADE, to='Contribuyentes.Contribuyente', verbose_name='Contribuyente')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Solicitud143_Step2f',
                'verbose_name_plural': 'Solicitud143_Step2f',
                'unique_together': {('contribuyente', 'num_expediente')},
            },
        ),
        migrations.CreateModel(
            name='Solicitud143_Step2e',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.BigIntegerField(blank=True, null=True)),
                ('num_expediente', models.BigIntegerField(default=Solicitudes.models.Solicitud143_Step2e.Incrementar, verbose_name='Numero de Expediente')),
                ('ind_sect_SI', models.BooleanField(default=False, help_text='Servicios e Infraestructura', verbose_name='Servicios e Infraestructura')),
                ('ind_sect_CES', models.BooleanField(default=False, help_text='Certificación de edificios sostenibles', verbose_name='Certificación de edificios sostenibles')),
                ('ind_sect_FCC', models.BooleanField(default=False, help_text='Formación continua y capacitación', verbose_name='Formación continua y capacitación')),
                ('ind_sect_ERV', models.BooleanField(default=False, help_text='Energías renovables de vanguardia', verbose_name='Energías renovables de vanguardia')),
                ('ind_sect_DMC', models.BooleanField(default=False, help_text='Desarrollo de mercado de capitales', verbose_name='Desarrollo de mercado de capitales')),
                ('contribuyente', models.ForeignKey(help_text='Contribuyente', on_delete=django.db.models.deletion.CASCADE, to='Contribuyentes.Contribuyente', verbose_name='Contribuyente')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Solicitud143_Step2e',
                'verbose_name_plural': 'Solicitud143_Step2e',
                'unique_together': {('contribuyente', 'num_expediente')},
            },
        ),
        migrations.CreateModel(
            name='Solicitud143_Step2d',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.BigIntegerField(blank=True, null=True)),
                ('num_expediente', models.BigIntegerField(default=Solicitudes.models.Solicitud143_Step2d.Incrementar, verbose_name='Numero de Expediente')),
                ('ind_sect_NTPE', models.BooleanField(default=False, help_text='Nivel Tecnológico del producto elaborado', verbose_name='Nivel Tecnológico del producto elaborado')),
                ('ind_sect_STE', models.BooleanField(default=False, help_text='Sectores y tecnologías estrategicos', verbose_name='Sectores y tecnologías estrategicos')),
                ('ind_sect_SIN', models.BooleanField(default=False, help_text='Sello de la Industria Nacional', verbose_name='Sello de la Industria Nacional')),
                ('ind_sect_FCC', models.BooleanField(default=False, help_text='Formación continua y capacitación', verbose_name='Formación continua y capacitación')),
                ('ind_sect_ERV', models.BooleanField(default=False, help_text='Energías renovables de vanguardia', verbose_name='Energías renovables de vanguardia')),
                ('ind_sect_DMC', models.BooleanField(default=False, help_text='Desarrollo de mercado de capitales', verbose_name='Desarrollo de mercado de capitales')),
                ('contribuyente', models.ForeignKey(help_text='Contribuyente', on_delete=django.db.models.deletion.CASCADE, to='Contribuyentes.Contribuyente', verbose_name='Contribuyente')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Solicitud143_Step2d',
                'verbose_name_plural': 'Solicitud143_Step2d',
                'unique_together': {('contribuyente', 'num_expediente')},
            },
        ),
        migrations.CreateModel(
            name='Solicitud143_Step2c',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.BigIntegerField(blank=True, null=True)),
                ('num_expediente', models.BigIntegerField(default=Solicitudes.models.Solicitud143_Step2c.Incrementar, verbose_name='Numero de Expediente')),
                ('ind_sect_FCC', models.BooleanField(default=False, help_text='Formación continua y capacitación', verbose_name='Formación continua y capacitación')),
                ('ind_sect_DPP', models.BooleanField(default=False, help_text='Diferenciación de productos y procesos', verbose_name='Diferenciación de productos y procesos')),
                ('ind_sect_ERV', models.BooleanField(default=False, help_text='Energías renovables de vanguardia', verbose_name='Energías renovables de vanguardia')),
                ('ind_sect_DMC', models.BooleanField(default=False, help_text='Desarrollo de mercado de capitales', verbose_name='Desarrollo de mercado de capitales')),
                ('contribuyente', models.ForeignKey(help_text='Contribuyente', on_delete=django.db.models.deletion.CASCADE, to='Contribuyentes.Contribuyente', verbose_name='Contribuyente')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Solicitud143_Step2c',
                'verbose_name_plural': 'Solicitud143_Step2c',
                'unique_together': {('contribuyente', 'num_expediente')},
            },
        ),
        migrations.CreateModel(
            name='Solicitud143_Step2b',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.BigIntegerField(blank=True, null=True)),
                ('num_expediente', models.BigIntegerField(default=Solicitudes.models.Solicitud143_Step2b.Incrementar, verbose_name='Numero de Expediente')),
                ('ind_gral_empleo', models.BooleanField(default=False, help_text='Generación de empleo', verbose_name='Generación de empleo')),
                ('ind_gral_exportaciones', models.BooleanField(default=False, help_text='Aumento de exportaciones (en US$)', verbose_name='Aumento de exportaciones (en US$)')),
                ('ind_gral_descentralizacion', models.BooleanField(default=False, help_text='Descentralización', verbose_name='Descentralización')),
                ('ind_gral_TL', models.BooleanField(default=False, help_text='Utilización de tecnologías limpias', verbose_name='Utilización de tecnologías limpias')),
                ('ind_gral_IDi', models.BooleanField(default=False, help_text='Incremento de investigación, desarrollo e innovación (I+D+i)', verbose_name='Incremento de investigación, desarrollo e innovación (I+D+i)')),
                ('contribuyente', models.ForeignKey(help_text='Contribuyente', on_delete=django.db.models.deletion.CASCADE, to='Contribuyentes.Contribuyente', verbose_name='Contribuyente')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Solicitud143_Step2b',
                'verbose_name_plural': 'Solicitud143_Step2b',
                'unique_together': {('contribuyente', 'num_expediente')},
            },
        ),
    ]
