from django import forms
from models import Requst


class RequstForm(forms.Form):

    title = forms.CharField(max_length=30)
    content = forms.TextField(max_length=100)
    birth_date = forms.DateField(required=False)
    status = forms.CharField(max_length=10,widget=forms.Select(choices=status_CHOICES))

