from django import forms

class sendForm(forms.Form):
    to = forms.EmailField(label='To: ', max_length=200)
    name = forms.CharField(label="receiver's name: ", max_length=20)
    subject = forms.CharField(label='Subject: ', max_length=100)
    message = forms.CharField(label='Message: ', max_length=500)
