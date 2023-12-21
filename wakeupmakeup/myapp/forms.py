from django import forms
from .models import Profile, Customer


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email']


class UserCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'address', 'phone', 'state', 'city']
