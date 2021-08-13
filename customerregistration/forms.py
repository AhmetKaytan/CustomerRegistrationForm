from django import forms
from django.db.models import fields
from .models import Customer


class CustomerForm(forms.ModelForm):

    class Meta ():
        model = Customer
        fields = [
            'tc_no', 'name', 'surname',
            'phone_no', 'city', 'district'
        ]