from .models import FirstData
from django import forms

class Form_page(forms.ModelForm):
    class Meta:
        model = FirstData
        fields = ['Customer_Name', 'Customer_Detail', 'Mail_ID', 'Service_ID', 'Service_Type',
                  'Problem_Description', ]
