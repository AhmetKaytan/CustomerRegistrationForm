from django.contrib import admin
from .models import Customer

class FormAdmin (admin.ModelAdmin):

    list_display = ['tc_no', 'name', 'surname', 'phone_no', 'city', 'district', 'registration_date']
    search_fields = ['id', 'tc_no', 'name', 'surname', 'phone_no', 'city', 'district']

    class Meta:
        model = Customer

admin.site.register(Customer, FormAdmin)
