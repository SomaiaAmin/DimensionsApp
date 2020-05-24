from django.db import models

# Create your models here.
class PhotoToBeMeasured(models.Model):
    left_most_width = models.FloatField()
    main_photo = models.ImageField(upload_to='images_to_measure/')
