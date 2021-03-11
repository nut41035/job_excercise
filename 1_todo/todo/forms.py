from django import forms

class todoForm(forms.Form):
    item = forms.CharField(label='Task: ', max_length=200)
    
class change(forms.Form):
    item_id = forms.CharField()