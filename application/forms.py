from django import forms
from .models import Empreco

class String(forms.Form):
    string1=forms.CharField(label='string1')
    string2=forms.CharField(label='string2')
    
    
class Contact(forms.Form):
    char_string=forms.CharField(label='Character string')
    int_string=forms.CharField(label='Integer string')
    
class Emprecords(forms.ModelForm):
    class Meta:
        model=Empreco
        fields='__all__'
        
class Scform(forms.Form):
    char_string=forms.CharField(label='character_string')
    int_string=forms.CharField(label='int_string')