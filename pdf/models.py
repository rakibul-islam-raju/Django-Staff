from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pdf')
    descroption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
