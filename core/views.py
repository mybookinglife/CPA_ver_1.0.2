from django.shortcuts import render
from django.contrib import auth
from django.apps import apps
from django.http import HttpResponse
import json

# Create your views here.
from myusers.forms import UserCreationForm, UserLoginForm, CompanyCreationForm, PasswordRecoveryForm


def index(request):
    
    UserCreationform = UserCreationForm()
    UserLoginform = UserLoginForm()
    CompanyCreationform = CompanyCreationForm()
    PasswordRecoveryform = PasswordRecoveryForm()
    
    return render(request, 'core/index.html', {'user': auth.get_user(request), 
                                               'UserCreationform': UserCreationform, 
                                               'UserLoginForm': UserLoginform, 
                                               'CompanyCreationform': CompanyCreationform, 
                                               'PasswordRecoveryform': PasswordRecoveryform
                                               }
                  ) 
    
    
def filterchain_all(request, app_name, model_name, method_name, pk):
    Model = apps.get_model(app_name, model_name)
    obj = Model.objects.get(pk=pk)
    qs = getattr(obj, method_name)()
    results = list(qs)
    final = []
    for item in results:
        final.append({'value': item.pk, 'display': str(item)})
    return HttpResponse(json.dumps(final), content_type='application/json')