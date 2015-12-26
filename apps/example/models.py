from django.db import models
from django.utils.encoding import python_2_unicode_compatible


"""
Modelo 1 de ejemplo
"""
@python_2_unicode_compatible
class Model1(models.Model):
    text = models.CharField(max_length=200)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.text


"""
Modelo 2 de ejemplo
"""
@python_2_unicode_compatible
class Model2(models.Model):
    text = models.CharField(max_length=200)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.text


"""
Modelo 3 de ejemplo
"""
@python_2_unicode_compatible
class Model3(models.Model):
    text = models.CharField(max_length=200)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.text
