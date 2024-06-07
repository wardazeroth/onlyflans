
from django import forms

class OnlyflanForm(forms.Form):
    nombre = forms.CharField(max_length=10,
    widget = forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=40, 
    widget = forms.EmailInput(attrs={'class':'form-control'}))
    mensaje = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control'}))
    