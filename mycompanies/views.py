# coding=utf-8
from django.shortcuts import render, get_object_or_404
from mycompanies.models import Company
from myusers.models import MyUser
from system.models import Transactions
from mycompanies.forms import CompanyForm, LoginChangeForm
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import (get_user_model)
from django.http import HttpResponse
import json

import datetime
from rest_framework import viewsets
from mycompanies.serializers import CompanyListSerializer

# Create your views here.

def company_index(request):

    if request.user.is_authenticated():
        
        user = request.user
        if user.company_id == None:
            return HttpResponseRedirect("/")
        
        company = get_object_or_404(Company, pk=user.company_id)
        
        if request.method == "POST":
        
            form = CompanyForm(request.POST, instance=company)
            if form.is_valid():
                company = form.save(commit=False)
                company.save()
                return HttpResponseRedirect("/")
        else:
            company_form = CompanyForm(instance=company)
            context = {
                    'form': company_form,
                    'email': user.username,
                    'login_change_form': LoginChangeForm()
            }
            context.update(csrf(request))
             
        return render(request, 'company_index.html', context)

    else:
        return HttpResponseRedirect("/")

def login_change(request):

    if request.user.is_authenticated():
        user = request.user;
        if request.method == "POST":
            form = LoginChangeForm(request.POST)
            if form.is_valid():
                email = request.POST['email'].strip()
                if email == user.username:
                    response_data = {}
                    response_data['result'] = 'fasle'
                    response_data['msg'] = 'Please enter another e-mail'
                    return HttpResponse(
                                        json.dumps(response_data),
                                        content_type="application/json"
                                        )
                else:                    
                    try:
                        emaildb = MyUser.objects.get(email=email)
                    except:
                        emaildb = False
                    if emaildb:
                        response_data = {}
                        response_data['result'] = 'fasle'
                        response_data['msg'] = 'Company with this e-mail already exists. Please enter another e-mail'
                        return HttpResponse(
                                            json.dumps(response_data),
                                            content_type="application/json"
                                            )
                        email = emaildb
                    else:
                        uid = urlsafe_base64_encode(force_bytes(user.pk))
                        token = default_token_generator.make_token(user)
                        transaction_id = uid.decode("utf-8")+'-'+token
                         
                        send_mail('Change e-mail', 'http://127.0.0.1:8000/mycompanies/login_change/'+transaction_id+'/', 'my.mybookings.myservices@gmail.com',
                                  [email], fail_silently=False)
                        lifetime = datetime.datetime.utcnow() + datetime.timedelta(hours=2)
                        try:
                            current_transaction = Transactions.objects.get(transaction_id=transaction_id)
                        except:
                            current_transaction = False
                        if current_transaction:
                            current_transaction.email = email
                            current_transaction.lifetime = lifetime
                            current_transaction.save()
                        else:
                            Transactions.objects.create(transaction_id=transaction_id, email=email, lifetime=lifetime)
                        response_data = {}
                        response_data['result'] = 'true'
                        response_data['msg'] = 'e-mail sent'
                        return HttpResponse(
                                            json.dumps(response_data),
                                            content_type="application/json"
                                            )
                context = {
                        'form': form,
                        'email': email,
                }
                return TemplateResponse(request, 'email_change.html', context)
            return HttpResponseRedirect("/")
        else:
            form = LoginChangeForm()
            context = {
                    'form': form,
                    'email': user.username,
            }
            context.update(csrf(request))
            return TemplateResponse(request, 'login_change.html', context)
       
    else:
        return HttpResponseRedirect("/")
    

def login_change_confirm(request, uidb64=None, token=None,
                           template_name='login_change_confirm.html',
                           token_generator=default_token_generator,
                           post_reset_redirect=None):

    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    UserModel = get_user_model()
    assert uidb64 is not None and token is not None
    try:
        # urlsafe_base64_decode() decodes to bytestring on Python 3
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserModel._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None
    if user is not None and token_generator.check_token(user, token):
        validlink = True
        transaction_id=uidb64+'-'+token
        try:
            transaction = Transactions.objects.get(transaction_id=transaction_id)
        except:
            transaction = False
        if transaction:
#             if transaction.lifetime > datetime.datetime.utcnow():
            user.username = transaction.email
            user.email = transaction.email
            user.save()
            transaction.delete()
            return HttpResponseRedirect(post_reset_redirect)
        form = None
    else:
        validlink = False
        form = None
    context = {
        'form': form,
        'validlink': validlink,
    }
    return TemplateResponse(request, template_name, context)


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanyListSerializer
