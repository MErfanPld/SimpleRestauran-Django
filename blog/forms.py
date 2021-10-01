from django import forms

class CommetForm(forms.Form):
    fullname = forms.CharField(max_length=500)
    email = forms.EmailField()
    massage = forms.CharField(widget=forms.Textarea)