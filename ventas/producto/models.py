from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Producto(models.Model):
	titulo = models.CharField(max_length=100)
	descripcion = models.TextField()
	marca = models.CharField(max_length=100)
	modelo = models.CharField(max_length=100)
	precio=models.IntegerField()
	fecha = models.DateTimeField(default=timezone.now)
	foto1= models.ImageField(upload_to='media')
	foto2= models.ImageField(upload_to='media',blank=True)
	foto3= models.ImageField(upload_to='media',blank=True)
	foto4= models.ImageField(upload_to='media',blank=True)
	foto5= models.ImageField(upload_to='media',blank=True)
	autor =models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		return reverse('producto-detail',kwargs={'pk':self.pk})

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)

		img1=Image.open(self.foto1.path)
		img2=Image.open(self.foto2.path)
		img3=Image.open(self.foto3.path)
		img4=Image.open(self.foto4.path)
		img5=Image.open(self.foto5.path)

		if img1.height>1200 or img1.width>1200:
			output_size=(1200,1200)
			img1.thumbnail(output_size)
			img2.thumbnail(output_size)
			img1.save(self.foto1.path)
			img2.save(self.foto2.path)
