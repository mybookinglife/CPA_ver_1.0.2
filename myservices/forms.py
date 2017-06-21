from django import forms
from myservices.models import Service

class NewService(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('name', 'type_service', 'price', 'duration')
        
class EditService(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('name', 'type_service',  'price', 'duration', 'number_of_experts', 'is_active')
#         widgets = {
#             'name': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
#         }