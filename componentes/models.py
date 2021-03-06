from django.db import models
from django.core.validators import (MaxLengthValidator, MaxValueValidator,
                                    MinValueValidator,
                                    MinLengthValidator,
                                    RegexValidator)
LONGUITUD_MAXIMA = 'Error en la longitud'
LONGUITUD_MAXIMA_SALDO = 'Error en la longitud son 9 digitos los permitidos'
LONGITUD_MINIMA = 'Error de longitud mínima'
VALOR_MINIMO = 'El valor mínimo permitido es 1'
VALOR_MAXIMO_CAN = 'El valor máximo permitido son 100'
VALOR_MAXIMO = 'El valor máximo permitido son 100000000'
FORMATO_NUMERO_INCORRECTO = 'Formato inválido no deben ir numéros'
FORMATO_CARACTER_INCORRECTO = 'Formato sólo se aceptan letras :'


regexNumero = RegexValidator('^[0-9]*$', 'No se permiten letras')
regexCaracter = RegexValidator(
    r"^[A-Za-zÀ-ÿ\u00E0-\u00FC ]+$", 'No se permiten caracteres especiales')


# Create your models here.
class Componentes(models.Model):
    activo = models.BooleanField(default=True)
    nombre_componente = models.CharField(
        max_length=60, null=False, blank=False, default='',
        validators=[
            MaxLengthValidator(60, LONGUITUD_MAXIMA),
            MinLengthValidator(5, LONGITUD_MINIMA), regexCaracter])

    def __str__(self):
        return self.nombre_componente


class Actividades(models.Model):

    nombre_actividad = models.CharField(
        max_length=60, null=False, blank=False, default='',
        validators=[
            MaxLengthValidator(60, LONGUITUD_MAXIMA),
            MinLengthValidator(5, LONGITUD_MINIMA), regexCaracter])
    unidad_medida_presupuestal = models.CharField(
        max_length=60, null=False, blank=False, default='', validators=[
            MaxLengthValidator(60, LONGUITUD_MAXIMA),
            MinLengthValidator(5, LONGITUD_MINIMA), regexCaracter])
    cantidad = models.IntegerField(
        default=0, validators=[
            MaxValueValidator(100, 'El valor máximo permitido es 100'),
            MinValueValidator(1, VALOR_MINIMO)])
    recurso_disponible = models.DecimalField(
        max_digits=9, null=False, blank=False,
        decimal_places=2, default=0.0,
        validators=[
            MinValueValidator(1, VALOR_MINIMO),
            MaxValueValidator(100000000, VALOR_MAXIMO)])
    componente = models.ForeignKey(
        Componentes, verbose_name="Componentes",
        on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre_actividad
