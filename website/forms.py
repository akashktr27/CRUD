from django.contrib.auth.forms import forms, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder": "First Name", "class" :"form-control"}), label="")
    last_name = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder": "Last Name", "class" : 'form-control'}), label="")
    email = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder": "Email", "class": 'form-control'}), label="")
    phone = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder" : "Phone", "class" : 'form-control'}) ,label="")
    address = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder" : "Address", "class" : 'form-control'}), label="")
    city = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder" : "city", "class" : 'form-control'}), label="")
    state = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder" : "State", "class" : 'form-control'}), label="")
    zipcode = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder" : "Zipcode", "class" : 'form-control'}), label="")

    class Meta:
        model = Record
        exclude = ("user", )
