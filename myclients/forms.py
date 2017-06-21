from django import forms
from myclients.models import Client

class NewClient(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'phone', 'email', 'is_vip')
        
class EditClient(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'firstname', 'lastname', 'middlename', 'phone', 'email', 'is_vip', 'note')
#         widgets = {
#             'name': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
#         }