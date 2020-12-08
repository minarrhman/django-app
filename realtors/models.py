from django.db import models

class Realtor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    descrption = models.TextField(blank=True)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateField(blank=True)
    def __str__(self):
        return self.name
