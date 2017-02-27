from django import forms

class PaymentForm(forms.Form):
    id = forms.IntegerField("id")
    amount = forms.DecimalField("Amount", max_digits=12, decimal_places=2)
    date = forms.DateField("Date")