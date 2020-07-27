from django.db import models
import datetime

class ShiftLog(models.Model):
    owner = models.ForeignKey('auth.User', related_name='shift_logs', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    log = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
