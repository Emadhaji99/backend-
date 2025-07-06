from django import forms
class content(forms.Form):
    task=forms.CharField(label="new task")