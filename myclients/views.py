# coding=utf-8
from django.shortcuts import render, get_object_or_404
from myclients.models import Client
from django.template.context_processors import csrf
from django.http import HttpResponse
from myclients.forms import NewClient
from myclients.forms import EditClient
import json
from myusers.models import MyUser
import logging
from rest_framework import viewsets
from myclients.serializers import ClientListSerializer

# Create your views here.

def add_client(request):

    if request.method == "POST":

        form = NewClient(request.POST)

        if form.is_valid():
            object_client = form.save(commit=False)
            try:
                object_user = MyUser.objects.get(username=object_client.phone);
                object_client.user = object_user
                object_client.firstname = object_user.firstname
                object_client.lastname = object_user.lastnames
                object_client.middlename = object_user.middlename
            except Exception as msg:
                logger = logging.getLogger(__name__)
                logger.exception(msg)
            
            object_client.company = request.user.company
            object_client.save()

            response_data = {}
            response_data['result'] = 'true'
            response_data['id'] = object_client.id
            response_data['name'] = object_client.name

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
        form = NewClient()



def edit_client(request, client_id):

    if request.method == "POST":

        client = get_object_or_404(Client, pk=int(client_id))
        form = EditClient(request.POST, instance=client)

        if form.is_valid():
            object_client = form.save(commit=False)
            try:
                object_user = MyUser.objects.get(username=object_client.phone);
                object_client.user = object_user;

            except Exception as msg:
                object_client.user = None
                logger = logging.getLogger(__name__)
                logger.exception(msg)
            
            object_client.company = request.user.company
            object_client.save()

            response_data = {}
            response_data['result'] = 'true'
            response_data['id'] = object_client.id
            response_data['name'] = object_client.name

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

        form = EditClient()



def delete_client(request, client_id):

    if request.method == 'POST':

        client = get_object_or_404(Client, pk=client_id)
        client.delete()

        response_data = {}
        response_data['result'] = 'true'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def get_info_client(request, client_id):

    if request.method == 'POST':

        client = get_object_or_404(Client, pk=client_id)
        form_edit_client = EditClient(instance=client)

        response_data = {}
        response_data.update(csrf(request))
        response_data['form_edit_client'] = form_edit_client

        return HttpResponse(
            render(request, 'client_form_edit.html', response_data))

    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def list_clients(request, value_filter = "all"):

    if value_filter == 'all':
        clients_list = Client.objects.filter(company=request.user.company)
    elif value_filter == 'is_vip':
        clients_list = Client.objects.filter(is_vip=True, company=request.user.company)
    elif value_filter == 'is_not_vip':
        clients_list = Client.objects.filter(is_vip=False, company=request.user.company)
    else:
        clients_list = Client.objects.filter(pk=0, company=request.user.company)

    if request.method == "POST":

        response_data = {}
        response_data.update(csrf(request))
        response_data['clients_list'] = clients_list

        return HttpResponse(
            render(request, 'clients_list.html', response_data))

    else:

        return render(request, 'clients_index.html', {
            'clients_list': clients_list,
            'form_new_client': NewClient(),
            'form_edit_client': EditClient()
        }
        )

class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Client.objects.all()
    serializer_class = ClientListSerializer