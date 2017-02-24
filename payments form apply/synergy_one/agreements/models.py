from django.db import models

# Create your models here.
class Agreement(models.Model):
    _id = models.IntegerField(unique=True)

    change_form_template = "admin/agreements_change_form.html"


class Payment(models.Model):
    agreement = models.ForeignKey(Agreement)
    _id = models.IntegerField(unique=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()