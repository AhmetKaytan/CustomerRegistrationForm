from django import forms
from django.db.models import fields
from django.forms.widgets import Select
from .models import Customer


class CustomerForm(forms.ModelForm):

    class Meta ():
        model = Customer
        fields = [
            'tc_no', 'name', 'surname',
            'phone_no', 'city', 'district'
        ]

class paginationForm(forms.Form):
    choices = [
        '3', '5', '15',
        '25', '50'
    ]
    select=forms.ChoiceField(widget=forms.Select(choices=choices))