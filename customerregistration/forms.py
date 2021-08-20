from django import forms

from .models import Customer



class CustomerForm(forms.ModelForm):

    class Meta ():
        model = Customer
        fields = [
            'tc_no', 'name', 'surname',
            'phone_no', 'city', 'district'
        ]
        
        
    def clean(self):
        cleaned_data = super().clean()
        data_tc_no = cleaned_data.get('tc_no')
        data_phone_no = cleaned_data.get('phone_no')

        if data_phone_no and data_tc_no:
            if (len(data_tc_no) != 11 
            or len(data_phone_no) != 11):
                raise forms.ValidationError("Info is incorrect")
        else:
            return None