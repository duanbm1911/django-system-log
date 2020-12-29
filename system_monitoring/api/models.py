from django.db import models

# Create your models here.

class SystemLogModel(models.Model):
    time = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    device = models.CharField(max_length=200)
    log = models.CharField(max_length=2000)

    def __str__(self):
        return self.device