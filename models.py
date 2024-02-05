from django.db import models
# Crete yur models here 

class Libro(models.Model):
  titulo = models.CharField(max_length=200)
  autor = models.CharField(max_length=100)
  resumen = models.TextField()

def __str__(self):
  return self.titulo
  