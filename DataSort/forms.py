from django import forms

class ip_array(forms.Form):
    array = forms.CharField(label='array',max_length=200)