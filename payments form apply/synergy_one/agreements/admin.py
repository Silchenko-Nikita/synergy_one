import json

from django import forms
from django.contrib import admin

# Register your models here.
from django.core.exceptions import MultipleObjectsReturned
from django.forms import formset_factory

from agreements.forms import PaymentForm
from agreements.utils import UnauthorizedError, get_formset, get_payments_list, \
    get_payments_list_from_local
from .models import Agreement
import requests


IP = "127.0.0.1:8000/agreements"
my_uuid = 'f9825a6c-c3c9-469a-bd38-e118cf4e8fe7'


class AgreementAdmin(admin.ModelAdmin):
    fields = ('external_id',)
    change_form_template = "admin/agreements_change_form.html"

    def change_view(self, request, object_id, extra_context=None, **kwargs):
        extra_context = extra_context or {}
        try:
            obj = Agreement.objects.get(id=object_id)
        except Agreement.DoesNotExist:
            print("Have not got agreement with id {0}".format(object_id))
            return super(AgreementAdmin, self).change_view(request, object_id,
                                                           extra_context=extra_context)
        except MultipleObjectsReturned:
            print("Several agreement with id {0}".format(object_id))
            return super(AgreementAdmin, self).change_view(request, object_id,
                                                           extra_context=extra_context)

        try:
            payments_list = get_payments_list_from_local(obj.external_id, my_uuid) # or get_payments_list(IP, obj.external_id, my_uuid)
        except UnauthorizedError:
            print("Invalid GUID!")
            return super(AgreementAdmin, self).change_view(request, object_id,
                                                    extra_context=extra_context)

        payments_got = True if payments_list else False
        payment_formset = get_formset(PaymentForm, payments_list)

        extra_context['payment_formset'] = payment_formset
        extra_context['payments_got'] = payments_got
        return super(AgreementAdmin, self).change_view(request, object_id,
                        extra_context=extra_context)


admin.site.register(Agreement, AgreementAdmin)
