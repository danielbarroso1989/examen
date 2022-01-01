from django import forms

class Companyform(forms.Form):
    name = forms.CharField(label='name', max_length=50, required=True,)
    description = forms.CharField(label='description', max_length=100, required=True,)
    symbol = forms.CharField(label='symbol', max_length=10, required=True,)
    values = forms.CharField(label='values', required=True,)
 