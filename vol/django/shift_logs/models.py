from django.db import models
import datetime

class ShiftLog(models.Model):
    name = models.CharField(max_length=250)
    log = models.CharField(max_length=500)
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
