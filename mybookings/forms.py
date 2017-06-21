from django import forms
from core.widgets import ChainedSelectWidget
from myclients.models import Client
from myservices.models import Service
from myexperts.models import Expert
from mybookings.models import Booking

class NewBooking(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('date_time', 'company','client', 'service', 'expert')
        
#     mycompanies = forms.ModelChoiceField(queryset=Company.objects.all())
#     myclients = forms.ModelChoiceField(queryset=Client.objects.all())
#     myservices = forms.ModelChoiceField(queryset=Service.objects.all())
#     myexperts = forms.ModelChoiceField(queryset=Expert.objects.all())
    
    def __init__(self, *args, **kwargs):
        super(NewBooking, self).__init__(*args, **kwargs)
  
        if 0 == len(self.data):
            # clear queryset if we just show a form
            self.fields['client'].queryset = Client.objects.none()
            self.fields['service'].queryset = Service.objects.none()
            self.fields['expert'].queryset = Expert.objects.none()
  
        # assign a widget to second select field
        self.fields['client'].widget = ChainedSelectWidget(
            id_field = 'id_client', 
            parent_name='company',         # the name of parent field
            app_name='mycompanies',            # the name of model's application
            model_name='Company',          # the name of a model with the method
            method_name='get_client_company', # the name of queryset method
            )        
                  
        self.fields['myservices'].widget = ChainedSelectWidget(
            id_field = 'id_service',   
            parent_name='company',         # the name of parent field
            app_name='mycompanies',            # the name of model's application
            model_name='Company',          # the name of a model with the method
            method_name='get_service_company', # the name of queryset method
            )        
  
        self.fields['expert'].widget = ChainedSelectWidget(
            id_field = 'id_expert',        
            parent_name='service',         # the name of parent field
            app_name='myservices',            # the name of model's application
            model_name='Service',          # the name of a model with the method
            method_name='get_expert_services', # the name of queryset method
            )        

         
class EditBooking(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('date_time', 'company', 'client', 'service', 'expert', 'note', 'comment', 'is_new')
  
#     mycompanies = forms.ModelChoiceField(queryset=Company.objects.all())
    client = forms.ModelChoiceField(queryset=Client.objects.all())
    service = forms.ModelChoiceField(queryset=Service.objects.all())
    expert = forms.ModelChoiceField(queryset=Expert.objects.all())      
    
    def __init__(self, *args, **kwargs):
        super(EditBooking, self).__init__(*args, **kwargs)

        if 0 == len(self.data):
            # clear queryset if we just show a form
            self.fields['client'].queryset = Client.objects.all()
            self.fields['service'].queryset = Service.objects.all()
            self.fields['expert'].queryset = Expert.objects.all()

        # assign a widget to second select field
        self.fields['client'].widget = ChainedSelectWidget(
            id_field = 'id_client', 
            parent_name='company',         # the name of parent field
            app_name='mycompanies',            # the name of model's application
            model_name='Company',          # the name of a model with the method
            method_name='get_client_company', # the name of queryset method
            )        
                 
        self.fields['service'].widget = ChainedSelectWidget(
            id_field = 'id_service',   
            parent_name='company',         # the name of parent field
            app_name='mycompanies',            # the name of model's application
            model_name='Company',          # the name of a model with the method
            method_name='get_service_company', # the name of queryset method
            )        
 
        self.fields['expert'].widget = ChainedSelectWidget(
            id_field = 'id_expert',        
            parent_name='service',         # the name of parent field
            app_name='myservices',            # the name of model's application
            model_name='Service',          # the name of a model with the method
            method_name='get_expert_services', # the name of queryset method
            )        
                
      
        