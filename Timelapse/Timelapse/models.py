from django.db import models

class TimelapseImage(models.Model):
    imageName = models.CharField(max_length=256)
    image = models.ImageField(upload_to='Timelapse/Images')