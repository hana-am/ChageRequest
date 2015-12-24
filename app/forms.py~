
from django import forms
from models import Requst

class RequstForm(forms.ModelForm):
    class Meta:
        model = Requst
        fields = ['title', 'content', 'pub_date' , 'status']


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)


