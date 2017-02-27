import json

from django.http import HttpResponse
from django.shortcuts import render

from agreements.utils import get_payments_list_from_data, HTTP_NO_CONTENT
import os.path

HTTP_OK = 200

payments_data_path = os.path.abspath(os.path.join(__file__, os.pardir)) + '/data/payments.json'
# Create your views here.

def test_payments_return(request, agr_id):
    # if request token header was not my_uuid
    # HttpResponse("", status_code=HTTP_UNAUTHORIZED)
    payms_list = get_payments_list_from_data(payments_data_path, agr_id)
    if payms_list:
        return HttpResponse(json.dumps(payms_list), status=HTTP_OK)
    else:
        return HttpResponse("[]", status=HTTP_NO_CONTENT)
