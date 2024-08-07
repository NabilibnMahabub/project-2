from django import forms
from . import views

#making forms
class Contact_Form(forms.Form):
    name = forms.CharField(max_length=64)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
    def send_email(self):
        print(f'sending email from {self.cleaned_data["email"]} with message {self.cleaned_data["message"]}')