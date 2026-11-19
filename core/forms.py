
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Complaint


# CUSTOMER REGISTRATION FORM
class CustomerRegistrationForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Enter your first name'
        })
    )

    last_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Enter your last name'
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'Enter your email address'
        })
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Choose a username'
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Create a password'
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Confirm your password'
        })
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        ]


# COMPLAINT SUBMISSION FORM
class ComplaintForm(forms.ModelForm):

    class Meta:
        model = Complaint

        fields = [
            'category',
            'subject',
            'description',
            'address',
            'contact_number',
        ]

        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-input',
            }),

            'subject': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter complaint subject',
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Describe your electricity issue',
                'rows': 5,
            }),

            'address': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Enter the location of the electricity issue',
                'rows': 3,
            }),

            'contact_number': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter your contact number',
            }),
        }
