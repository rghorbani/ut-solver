from django import forms
from django.forms import fields

class NewProblemForm(forms.ModelForm):
    problem_text = fields.TextInput()