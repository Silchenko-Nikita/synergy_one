from django.contrib import admin

# Register your models here.
from .models import Agreement, Payment


class PaymentAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'amount', 'date')


admin.site.register(Agreement)
admin.site.register(Payment, PaymentAdmin)