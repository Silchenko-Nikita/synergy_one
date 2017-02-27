from django.db import models

# Create your models here.
class Agreement(models.Model):
    external_id = models.IntegerField(unique=True)
    date = models.DateField(auto_now=True)
