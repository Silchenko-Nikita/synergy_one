from django import forms

from agreements.models import Payment


class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        exclude = ("agreement",)