from django.conf.urls import url

from agreements.views import test_payments_return

urlpatterns = [
    url(r'API/VI/agreements/(?P<agr_id>\d+)/payment/$', test_payments_return),
]