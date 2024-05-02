from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    content = models.TextField()
    # img = models.ImageField(upload_to='photo/%y/%m/%d')
    active = models.BooleanField(default='True')