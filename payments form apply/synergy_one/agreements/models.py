from django.db import models

# Create your models here.
class Agreement(models.Model):
    _id = models.IntegerField(unique=True)

    change_form_template = "admin/agreements_change_form.html"


class Payment(models.Model):
    agreement = models.ForeignKey("Agreement", Agreement)
    _id = models.IntegerField("id", unique=True)
    amount = models.DecimalField("Amount", max_digits=12, decimal_places=2)
    date = models.DateField("Date")