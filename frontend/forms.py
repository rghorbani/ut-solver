from models import *
from django import forms
from django.forms import fields
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    first_name = fields.CharField(required=True, max_length=30)
    last_name = fields.CharField(required=True, max_length=30)
    email = fields.EmailField(required=True)

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):
    first_name = fields.CharField(required=True, max_length=30)
    last_name = fields.CharField(required=True, max_length=30)
    # first_name = fields.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}), label='First Name', max_length=30)
    # last_name = fields.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}), label='Last Name', max_length=30)
    email = fields.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class NewProblemForm(forms.ModelForm):
    problem_text = fields.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter the Problem', 'class': 'form-control'}), label='Problem')

    class Meta:
        model = Problem
        fields = ('problem_text',)