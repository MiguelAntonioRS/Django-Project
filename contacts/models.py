from django.db import models

class Contact(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=8, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)