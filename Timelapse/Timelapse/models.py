from django.db import models

class TimelapseImage(models.Model):
    date = models.DateField(default='2021-01-01')
    time = models.TimeField(default='00:00')
    image = models.ImageField(upload_to='Timelapse/Images')