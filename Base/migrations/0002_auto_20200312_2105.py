# Generated by Django 2.2.9 on 2020-03-13 00:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipogiro',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tipocontribuyente',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tipo_documento',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='subcategoria_inversiones',
            name='categoria',
            field=models.ForeignKey(help_text='Categorias de Inversiones', on_delete=django.db.models.deletion.CASCADE, related_name='has_categorias', to='Base.Categoria_Inversiones', verbose_name='Categorias de Inversiones'),
        ),
        migrations.AddField(
            model_name='subcategoria_inversiones',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pais',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ministerios',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='localidad',
            name='departamento',
            field=models.ForeignKey(help_text='Departamento', on_delete=django.db.models.deletion.CASCADE, related_name='has_departamento', to='Base.Departamento', verbose_name='Departamento'),
        ),
        migrations.AddField(
            model_name='localidad',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='girociiu',
            name='tipo_giro',
            field=models.ForeignKey(help_text='Tipo Giro CIIU', on_delete=django.db.models.deletion.CASCADE, related_name='has_giro', to='Base.TipoGiro', verbose_name='Tipo Giro CIIU'),
        ),
        migrations.AddField(
            model_name='girociiu',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fechabalance',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='departamento',
            name='pais',
            field=models.ForeignKey(help_text='Pais', on_delete=django.db.models.deletion.CASCADE, related_name='has_paises', to='Base.Pais', verbose_name='Pais'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='categoria_inversiones',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='subcategoria_inversiones',
            unique_together={('categoria', 'subcategoria')},
        ),
        migrations.AlterUniqueTogether(
            name='localidad',
            unique_together={('departamento', 'descripcion')},
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('pais', 'descripcion')},
        ),
    ]