from django.db import models

# Create your models here.
class Empreco(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField()
    class Meta:
        db_table='Empreco'