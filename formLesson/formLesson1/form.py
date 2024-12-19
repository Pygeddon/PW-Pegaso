from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea( attrs={'placeholder': 'Your message'}))