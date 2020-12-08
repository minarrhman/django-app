from django.db import models
from datetime import datetime
from realtors.models import Realtor
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_length=1, decimal_places=1, max_digits=2)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_length=4, decimal_places=1, max_digits=4)
    image_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    image1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title


