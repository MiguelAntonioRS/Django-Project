from django.db import models

class Contact(models.Model):
    
    avatar = models.ImageField(null=True, blank=True, upload_to='contact')
    name = models.CharField(max_length=100, verbose_name='Nombre')
    email = models.EmailField(max_length=50)
    birth_date = models.DateField(null=True, blank=True, verbose_name='Fecha de Nacimiento')
    phone = models.CharField(max_length=8, null=True, blank=True, verbose_name='Numero de telefono')
    created = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.name