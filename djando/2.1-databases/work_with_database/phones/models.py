from django.db import models
# from django.utils.text import slugify

class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.URLField(max_length=500)
    release_date = models.DateTimeField()
    lte_exists = models.BooleanField(default = False)
    slug = models.SlugField(unique=True)

    
