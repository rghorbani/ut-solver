from models import *
from django import forms
from django.forms import fields
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    first_name = fields.CharField(required=True, max_length=30)
    last_name = fields.CharField(required=True, max_length=30)
    email = fields.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_username(self):
        try:
            User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']

        raise forms.ValidationError("Username is taken.")


class UserProfileForm(forms.ModelForm):
    first_name = fields.CharField(required=True, max_length=30)
    last_name = fields.CharField(required=True, max_length=30)
    # first_name = fields.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}), label='First Name', max_length=30)
    # last_name = fields.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}), label='Last Name', max_length=30)
    email = fields.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        try:
            self.fields['first_name'].initial = self.instance.first_name
            self.fields['last_name'].initial = self.instance.last_name
            self.fields['email'].initial = self.instance.email
        except User.DoesNotExist:
            pass

    # def save(self, *args, **kwargs):
    #     super(UserProfileForm, self).save(*args, **kwargs)
    #     self.instance.first_name = self.cleaned_data['first_name']
    #     self.instance.last_name = self.cleaned_data['last_name']


class NewProblemForm(forms.ModelForm):
    problem_text = fields.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter the Problem', 'class': 'form-control'}), label='Problem', error_messages={'required': 'You should choose one type.'})

    class Meta:
        model = Problem
        fields = ('problem_text',)


class UploadFileForm(forms.Form):
    file = forms.FileField(label='CUDA file')


class SolveCudaForm(forms.Form):
    CHOICES = (
        ('max', 'Max'),
        ('min', 'Min'),
    )

    choice = forms.MultipleChoiceField(choices = CHOICES, label='Choice', error_messages={'required': 'You should choose one type.'})

    def __init__(self, *args, **kwargs):
        super(SolveCudaForm, self).__init__(*args, **kwargs)
        self.initial['choice'] = 'max'