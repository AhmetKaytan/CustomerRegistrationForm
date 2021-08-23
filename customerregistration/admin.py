from django.contrib import admin
from .models import customer

class formAdmin (admin.ModelAdmin):

    list_display = ['tc_no', 'name', 'surname', 'phone_no', 'city', 'district', 'registration_date']
    search_fields = ['id', 'tc_no', 'name', 'surname', 'phone_no', 'city', 'district']

    class Meta:
        model = customer

admin.site.register(customer, formAdmin)
