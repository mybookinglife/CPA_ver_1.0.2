from django import forms
from mycompanies.models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'legal_name', 'itn', 'phone', 'legal_address', 'actual_address', 'activity', 'description', 'full_description', 'schedule', 'language', 'timezone')
        
class LoginChangeForm(forms.Form):
    email = forms.CharField(label='E-mail', widget=forms.EmailInput)