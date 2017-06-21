from django import forms
from myexperts.models import Expert

class NewExpert(forms.ModelForm):
    class Meta:
        model = Expert
        fields = ('name', 'phone', 'short_description')
        
class EditExpert(forms.ModelForm):
    class Meta:
        model = Expert
        fields = ('name', 'phone',  'short_description', 'description', 'is_active')
#         widgets = {
#             'name': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
#         }