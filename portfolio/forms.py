
from django.forms import ModelForm
from django import forms
from portfolio.models import Art

class Upload(ModelForm):
    class Meta:
       Model = Art
       field = '__all__'

class ContactMe(forms.Form):
    name = forms.CharField(max_length= 50)
    subject = forms.CharField(max_length= 50)
    sender = forms.EmailField()
    message = forms.CharField(widget= forms.Textarea)
    cc_myself = forms.BooleanField(required= False)