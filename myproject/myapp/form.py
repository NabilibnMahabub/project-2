from django import forms
from django.contrib.auth.models import User

#resitrarion form
class Resiter_Form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields  = ['username']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        # Check if the passwords match
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data
    
    


#making forms
class Contact_Form(forms.Form):
    name = forms.CharField(max_length=64)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
    def send_email(self):
        print(f'sending email from {self.cleaned_data["email"]} with message {self.cleaned_data["message"]}')