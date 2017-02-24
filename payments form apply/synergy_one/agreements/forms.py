from django import forms

from agreements.models import Payment


class PaymentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['agreement'].widget.attrs['readonly'] = True
        self.fields['_id'].widget.attrs['readonly'] = True
        self.fields['amount'].widget.attrs['readonly'] = True
        self.fields['date'].widget.attrs['readonly'] = True

    class Meta:
        model = Payment