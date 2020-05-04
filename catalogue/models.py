from django.db import models

# Create your models here.
class Catalogue(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

class FullDocument(models.Model):
    catalogue = models.ForeignKey(Catalogue, related_name='catalogue')
    document_text = models.TextField(default="")
    premium = models.BooleanField(default=True)

    def __str__(self):
        return self.catalogue.name

    