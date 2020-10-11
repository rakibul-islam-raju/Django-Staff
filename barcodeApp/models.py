from django.db import models
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File


class Product(models.Model):
    name = models.CharField(max_length=100)
    barcode = models.ImageField(upload_to='barcode', blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN('001718925923', writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save('barcode.png', File(buffer), save=False)
        return super().save(*args, **kwargs)
