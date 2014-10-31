from models import *
from django import forms
from django.forms import fields


class NewProblemForm(forms.ModelForm):
    problem_text = fields.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter the Problem', 'class': 'form-control'}), label='Problem')

    class Meta:
        model = Problem
        fields = ('problem_text',)


class UserProfileForm(forms.ModelForm):
    first_name = fields.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}), label='First Name', max_length=30)
    last_name = fields.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}), label='Last Name', max_length=30)

    class Meta:
        model = Problem
        fields = ('problem_text',)