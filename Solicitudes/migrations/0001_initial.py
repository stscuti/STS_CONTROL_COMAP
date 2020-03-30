# Generated by Django 2.2.9 on 2020-03-13 00:05

import Solicitudes.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Base', '0001_initial'),
        ('Contribuyentes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud143_Step1',
            fields=[
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.BigIntegerField(blank=True, null=True)),
                ('num_expediente', models.BigIntegerField(default=Solicitudes.models.Solicitud143_Step1.Incrementar, primary_key=True, serialize=False, verbose_name='Numero de Expediente')),
                ('estado_solicitud', models.CharField(blank=True, help_text='Es el Estado de la Solicitud', max_length=50, null=True, verbose_name='Estado de la Solicitud')),
                ('asignado_solicitud', models.CharField(blank=True, help_text='A quien esta Asignada la Solicitud', max_length=50, null=True, verbose_name='Solicitud: Asignado a:')),
                ('observacion_solicitud', models.CharField(blank=True, help_text='Observacion de la Solicitud', max_length=50, null=True, verbose_name='Observacion de la Solicitud')),
                ('actividad_agropecuaria_datoseconomicos', models.BooleanField(default=False, help_text='¿La Empresa tiene Actividad Agropecuaria?', verbose_name='¿La Empresa tiene Actividad Agropecuaria?')),
                ('proyectos_previos_datoseconomicos', models.BooleanField(default=False, help_text='Ya cuenta con proyectos de inversión presentados ante la COMAP', verbose_name='Ya cuenta con proyectos de inversión presentados ante la COMAP')),
                ('empresa_nueva_empresanueva', models.BooleanField(default=False, help_text='¿Es empresa nueva?', verbose_name='¿Es empresa nueva?')),
                ('sin_facturacion_ult3ej_empresanueva', models.BooleanField(default=False, help_text='¿Sin facturación ultimos 3 ejercicios?', verbose_name='¿Sin facturación ultimos 3 ejercicios?')),
                ('empresa_vinculada_empresanueva', models.BooleanField(default=False, help_text='¿Se encuentra vinculada con otras empresas?', verbose_name='¿Se encuentra vinculada con otras empresas?')),
                ('empresa_vinculada_sin_factult3ej_empresanueva', models.BooleanField(default=False, help_text='¿Empresas vinculadas sin facturación en los últimos 3 ejercicios?', verbose_name='¿Empresas vinculadas sin facturación en los últimos 3 ejercicios?')),
                ('pyme_mype', models.BooleanField(default=False, help_text='¿Es PYME?', verbose_name='¿Es PYME?')),
                ('cantidad_empleados_mype', models.DecimalField(decimal_places=6, help_text='Cantidad de Empleados', max_digits=20, verbose_name='Cantidad de Empleados')),
                ('ventas_netas_UI_mype', models.DecimalField(decimal_places=6, help_text='Ventas Netas en UI', max_digits=20, verbose_name='Ventas Netas en UI')),
                ('ventas_netas_pesos_mype', models.DecimalField(decimal_places=6, help_text='Ventas Netas en $', max_digits=20, verbose_name='Ventas Netas en $')),
                ('controlada_mype', models.BooleanField(default=False, help_text='¿Esta Controlada?', verbose_name='¿Esta Controlada?')),
                ('controlada_superamyoe_mype', models.BooleanField(default=False, help_text='¿Empresa Controlante Supera los limites de MYPE?', verbose_name='¿Empresa Controlante Supera los limites de MYPE?')),
                ('grupo_economico_mype', models.BooleanField(default=False, help_text='¿Pertenece a un Grupo Económico?', verbose_name='¿Pertenece a un Grupo Económico?')),
                ('grupo_economico_supera_mype', models.BooleanField(default=False, help_text='¿El Grupo Económico supera los limites de MYPE?', verbose_name='¿El Grupo Económico supera los limites de MYPE?')),
                ('proyeccion_cantidad_empleados_mype', models.DecimalField(decimal_places=6, help_text='Proyección de Cantidad de empleos ejercicio siguiente a inicio de actividad', max_digits=20, verbose_name='Proyección de Cantidad de empleos ejercicio siguiente a inicio de actividad')),
                ('proyeccion_ventas_netas_UI_mype', models.DecimalField(decimal_places=6, help_text='Proyección de Ventas netas en UI ejercicio siguiente inicio de actividad', max_digits=20, verbose_name='Proyección de Ventas netas en UI ejercicio siguiente inicio de actividad')),
                ('credito_fiscal_aportes_patronales_mype', models.BooleanField(default=False, help_text='¿Aplica crédito fiscal por aportes patronales de artículo 28º?', verbose_name='¿¿Aplica crédito fiscal por aportes patronales de artículo 28º??')),
                ('usuario_parque_industrial_mype', models.BooleanField(default=False, help_text='¿Usuario de Parque Industrial?', verbose_name='¿Usuario de Parque Industrial?')),
                ('objetivo_proyecto', models.CharField(blank=True, help_text='Objetivo del Proyecto', max_length=50, null=True, verbose_name='Objetivo del Proyecto')),
                ('informacion_ampliada_proyecto', models.TextField(blank=True, help_text='Informacion ampliada del Proyecto', max_length=50, null=True, verbose_name='Informacion ampliada del Proyecto')),
                ('extension_plazo_proyecto', models.BooleanField(default=False, help_text='¿Solicita extensión de plazo por lit a) artículo 4º?', verbose_name='¿Solicita extensión de plazo por lit a) artículo 4º?')),
                ('anos_ejecucion_inversion_proyecto', models.IntegerField(help_text='Años de ejecución de inversión', verbose_name='Años de ejecución de inversión')),
            ],
            options={
                'verbose_name': 'Solicitud143_Step1',
                'verbose_name_plural': 'Solicitud143_Step1',
            },
        ),
        migrations.CreateModel(
            name='Solicitud143_Step1b',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.BigIntegerField(blank=True, null=True)),
                ('num_expediente', models.BigIntegerField(default=Solicitudes.models.Solicitud143_Step1b.Incrementar, verbose_name='Numero de Expediente')),
                ('direccion', models.CharField(blank=True, help_text='Direccion de la Localizacion', max_length=50, null=True, verbose_name='Direccion')),
                ('numero_padron', models.CharField(blank=True, help_text='Numero de Padron', max_length=50, null=True, verbose_name='Numero de Padron')),
                ('localidad_ya_operaciones', models.BooleanField(default=False, help_text='¿Localidad donde ya se realizaban operaciones?', verbose_name='¿Localidad donde ya se realizaban operaciones?')),
                ('mejoras_fijas', models.BooleanField(default=False, help_text='¿Tiene mejoras fijas?', verbose_name='¿Tiene mejoras fijas?')),
                ('plazo_remanente_proyecto', models.IntegerField(help_text='Plazo remanente del contrato', verbose_name='Plazo remanente del contrato')),
                ('vinculacion_juridica_proyecto', models.CharField(blank=True, help_text='Vinculacion Juridica', max_length=50, null=True, verbose_name='Vinculacion Juridica')),
                ('contribuyente', models.ForeignKey(help_text='Contribuyente', on_delete=django.db.models.deletion.CASCADE, to='Contribuyentes.Contribuyente', verbose_name='Contribuyente')),
                ('departamento', models.ForeignKey(help_text='Departamento', on_delete=django.db.models.deletion.CASCADE, to='Base.Departamento', verbose_name='Departamento')),
                ('localidad', models.ForeignKey(help_text='Localidad', on_delete=django.db.models.deletion.CASCADE, to='Base.Localidad', verbose_name='Localidad')),
            ],
            options={
                'verbose_name': 'Solicitud143_Step1',
                'verbose_name_plural': 'Solicitud143_Step1',
            },
        ),
    ]