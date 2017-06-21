from django.shortcuts import render_to_response, render, redirect
from django.contrib import auth
# from django.conf.urls import url
# from django import forms as forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
# from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate as auth_authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

import json

from .forms import UserChangeForm, UserCreationForm, CompanyCreationForm, PasswordRecoveryForm

def profile(request):
    
    user = request.user
    if not user.is_authenticated():
        return redirect('login')
    
    if request.POST:
        {
         }
    else:
        form = UserChangeForm
        return render_to_response('registration/profile.html', {'user': auth.get_user(request),'form':form}) 

def add_user(request):
    
    if request.method == "POST":
        
        form = UserCreationForm(request.POST)
                
        if form.is_valid():
            User = form.save(commit=False)
#             Service.is_active = False
            #User.mycompanies = request.user.mycompanies
            User.save()

            response_data = {}
            response_data['result'] = 'true'
            response_data['id'] = User.id
            response_data['name'] = User.username

            return HttpResponse(
                    json.dumps(response_data),
                    content_type="application/json"
                    )
        
        else:
            return HttpResponse(
                                json.dumps({"nothing to see": "this isn't happening"}),
                                content_type="application/json"
                                ) 
    else:
        form = UserCreationForm()
    
    return render(request,'index.html', {'form': form}) 

def add_company(request):
    
    if request.method == "POST":
        
        form_user = UserCreationForm(request.POST)
        form_company = CompanyCreationForm(request.POST)
                
        if form_user.is_valid():
            if form_company.is_valid():
                Company = form_company.save(commit=False)
                Company.save() 
            
                User = form_user.save(commit=False)
                User.firstname = Company.name
                User.is_company = True
                User.company = Company
                User.save()
    
                response_data = {}
                response_data['result'] = 'true'
                response_data['id'] = User.id
                response_data['name'] = User.username
    
                return HttpResponse(
                        json.dumps(response_data),
                        content_type="application/json"
                        )
            else:
                return HttpResponse(
                                json.dumps({"nothing to see": "this isn't happening"}),
                                content_type="application/json"
                                )
        else:
            return HttpResponse(
                                json.dumps({"nothing to see": "this isn't happening"}),
                                content_type="application/json"
                                ) 
    else:
        form_user = UserCreationForm()
        form_company = CompanyCreationForm()
    
    return render(request,'index.html', {'form_user': form_user, 'form_company': form_company}) 
    
def login(request):
    
    user = auth_authenticate(username=request.POST['username'], password=request.POST['password'])
    
    if user is not None:
        auth_login(request, user)

        response_data = {}
        if user.is_active==True:
            response_data['result'] = True
        else:
            response_data['result'] = False
            auth_logout(request)    

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

    else:
        response_data = {}
        response_data['result'] = False

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

    
def password_recovery(request):
    form = PasswordRecoveryForm()

    if request.method == 'POST':
        data = PasswordRecoveryForm(request.POST)
        errors = data.is_valid()
        if not errors:
            #new_user = data.save()
            return HttpResponseRedirect("/")
    else:
        data, errors = {}, {}

    return render(request,"index.html", {
        'form' : form,
        })       
    
            