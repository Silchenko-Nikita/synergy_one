from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def test_payments_return(request, agr_id):
    if agr_id == "1":
        return HttpResponse("""[
            {
                "id": 20,
                "amount": 23.00,
                "date": "2017-03-24"
            },
            {
                "id": 21,
                "amount": 25.00,
                "date": "2017-03-25"
            }
        ]""")
    elif agr_id == "22":
        return HttpResponse("""[
            {
                "id": 10,
                "amount": 120.00,
                "date": "2017-04-17"
            }
        ]""")
    else:
        return HttpResponse("""{
                        "status": "empty"
                    }""")
