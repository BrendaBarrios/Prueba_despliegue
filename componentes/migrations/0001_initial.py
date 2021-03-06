# Generated by Django 2.2.7 on 2020-02-19 21:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Componentes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
                ('nombre_componente', models.CharField(default='', max_length=60, validators=[django.core.validators.MaxLengthValidator(60, 'Error en la longitud'), django.core.validators.MinLengthValidator(5, 'Error de longitud mínima'), django.core.validators.RegexValidator('^[A-Za-zÀ-ÿ\\u00E0-\\u00FC ]+$', 'No se permiten caracteres especiales')])),
            ],
        ),
        migrations.CreateModel(
            name='Actividades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_actividad', models.CharField(default='', max_length=60, validators=[django.core.validators.MaxLengthValidator(60, 'Error en la longitud'), django.core.validators.MinLengthValidator(5, 'Error de longitud mínima'), django.core.validators.RegexValidator('^[A-Za-zÀ-ÿ\\u00E0-\\u00FC ]+$', 'No se permiten caracteres especiales')])),
                ('unidad_medida_presupuestal', models.CharField(default='', max_length=60, validators=[django.core.validators.MaxLengthValidator(60, 'Error en la longitud'), django.core.validators.MinLengthValidator(5, 'Error de longitud mínima'), django.core.validators.RegexValidator('^[A-Za-zÀ-ÿ\\u00E0-\\u00FC ]+$', 'No se permiten caracteres especiales')])),
                ('cantidad', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100, 'El valor máximo permitido es 100'), django.core.validators.MinValueValidator(1, 'El valor mínimo permitido es 1')])),
                ('recurso_disponible', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, validators=[django.core.validators.MinValueValidator(1, 'El valor mínimo permitido es 1'), django.core.validators.MaxValueValidator(100000000, 'El valor máximo permitido son 100000000')])),
                ('componente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='componentes.Componentes', verbose_name='Componentes')),
            ],
        ),
    ]
