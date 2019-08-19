# models.py 
from django.db import models
class Hotel(models.Model): 
	name = models.CharField(max_length=50) 
	hotel_Main_Img = models.ImageField(upload_to='images/')

class Imagem(models.Model):
	arquivo = models.ImageField(upload_to='images/')


