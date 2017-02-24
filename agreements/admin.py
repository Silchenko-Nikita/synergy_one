import json

from django import forms
from django.contrib import admin

# Register your models here.

from .models import Agreement, Payment
import requests


class AgreementAdmin(admin.ModelAdmin):
    change_form_template = "admin/agreements_change_form.html"

    def change_view(self, request, object_id, extra_context=None, **kwargs):
        extra_context = extra_context or {}
        try:
            obj = Agreement.objects.get(id=object_id)
        except:
            print("Have not got agreement with id {0}".format(object_id))
            return super(AgreementAdmin, self).change_view(request, object_id,
                                                           extra_context=extra_context)

        payments_json = requests.get('http://ip/API/VI/agreements/{0}/payment'.format(obj._id))
        payments_list = json.loads(payments_json)
        # payment_forms_list will be constructed from payments_list
        # extra_context['payment_forms_list'] = payment_forms_list is to be parsed
        return super(AgreementAdmin, self).change_view(request, object_id,
                        extra_context=extra_context)


class PaymentAdmin(admin.ModelAdmin):
    pass
    # readonly_fields = ('_id', 'amount', 'date')


admin.site.register(Agreement, AgreementAdmin)
admin.site.register(Payment, PaymentAdmin)