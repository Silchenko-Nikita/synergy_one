from django.db import models

# Create your models here.
class Agreement(models.Model):
    _id = models.IntegerField(unique=True)


class Payment(models.Model):
    agreement = models.ForeignKey(Agreement)
    _id = models.IntegerField(unique=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()