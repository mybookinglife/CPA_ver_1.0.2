# coding: utf-8
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model

from mycompanies.models import Company

class UserCreationForm(forms.ModelForm):
    
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Сonfirm',
        widget=forms.PasswordInput
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Пароль и подтверждение не совпадают')
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'email','firstname', 'lastname', 'middlename')
        
class CompanyCreationForm(forms.ModelForm):
    username = forms.CharField(
        label='Login',
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Сonfirm',
        widget=forms.PasswordInput
    )

    def save(self, commit=True):
        company = super(CompanyCreationForm, self).save(commit=False)
        if commit:
            company.save()
        return company

    class Meta:
        model = Company
        fields = ('name','phone','activity')        


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField(
        widget=forms.PasswordInput,
        required=False
    )

    def save(self, commit=True):
        user = super(UserChangeForm, self).save(commit=False)
        password = self.cleaned_data["password"]
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['username',]


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
     
class PasswordRecoveryForm(forms.Form):
    email = forms.CharField(
        label='E-mail',
        widget=forms.EmailInput
    )