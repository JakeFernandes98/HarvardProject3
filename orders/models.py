from django.db import models

# Create your models here.

class RegPizza(models.Model):
    name = models.CharFiels(max_length=64)
    smallPrice = models.DecimalField(decimal_places=2)
    largePrice = models.DecimalField(decimal_places=2)

class SicPizza(models.Model):
    name = models.CharFiels(max_length=64)
    smallPrice = models.DecimalField(decimal_places=2)
    largePrice = models.DecimalField(decimal_places=2)

class Subs(models.Model):
    name = models.CharFiels(max_length=64)
    smallPrice = models.DecimalField(decimal_places=2)
    largePrice = models.DecimalField(decimal_places=2)

class Pasta(models.Model):
    name = models.CharFiels(max_length=64)
    price = models.DecimalField(decimal_places=2)

class Salads(models.Model):
    name = models.CharFiels(max_length=64)
    price = models.DecimalField(decimal_places=2)

class Platters(models.Model):
    name = models.CharFiels(max_length=64)
    smallPrice = models.DecimalField(decimal_places=2)
    largePrice = models.DecimalField(decimal_places=2)
