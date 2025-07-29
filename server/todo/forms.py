from django import forms
class content(forms.Form):
    email=forms.EmailField(max_length=30)
    age=forms.IntegerField(label="enter only number",max_value=20)
    