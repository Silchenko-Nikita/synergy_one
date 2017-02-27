import requests
from django.forms import formset_factory
from django.urls import reverse
import json

from synergy_one.settings import IP

HTTP_UNAUTHORIZED = 401
HTTP_NO_CONTENT = 204


class UnauthorizedError(Exception):

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


def get_payments_list(ip, agr_id, token):
    res = requests.get('http://{ip}/API/VI/agreements/{obj_id}/payment'.format(
        ip=ip, obj_id=agr_id), headers={'token': token})

    if res.status_code == HTTP_UNAUTHORIZED:
        raise UnauthorizedError

    payments_list = res.json() if res.text else []
    return payments_list


def get_payments_list_from_local(agr_id, token):
    res = requests.get('http://{ip}/{0}'.format(reverse("payments", kwargs={'agr_id': agr_id}), ip=IP),
                       headers={'token': token})

    if res.status_code == HTTP_UNAUTHORIZED:
        raise UnauthorizedError

    payments_list = res.json() if res.text else []
    return payments_list


def get_formset(form_class, obj_list):
    PaymentFormSet = formset_factory(form_class)
    payments_num = len(obj_list)
    data = {
        'form-TOTAL_FORMS': u'{0}'.format(payments_num),
        'form-INITIAL_FORMS': u'0',
        'form-MAX_NUM_FORMS': u'',
    }
    for i, obj in enumerate(obj_list):
        for k, v in obj.items():
            data['form-{0}-{1}'.format(i, k)] = v
    return PaymentFormSet(data)


def get_payments_list_from_data(file_path, agr_id):
    with open(file_path, 'r') as file:
        paym_json = file.read()
    id_payms_dict = json.loads(paym_json)
    for id, payms in id_payms_dict.items():
        if id == agr_id:
            return payms
    return []