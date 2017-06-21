# coding=utf-8
from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
#from django.template import Context, loader
from myservices.models import Service
from django.template.context_processors import csrf
from myservices.forms import NewService
from myservices.forms import EditService
from django.http import HttpResponse
import json
from myservices.serializers import ServiceSerializer
from rest_framework import viewsets
# Create your views here.


def add_service(request):

    if request.method == "POST":

        form = NewService(request.POST)

        if form.is_valid():
            object_Service = form.save(commit=False)
#             Service.is_active = False
            object_Service.company = request.user.company
            object_Service.save()

            response_data = {}
            response_data['result'] = 'true'
            response_data['id'] = object_Service.id
            response_data['name'] = object_Service.name

            return HttpResponse(
                json.dumps(response_data),
                content_type= "application/json"
            )

        else:
            return HttpResponse(
                json.dumps({"nothing to see": "this isn't happening"}),
                content_type="application/json"
            )
    else:
        form = NewService()

#     return render(request,'service_add.html', {'form': form})


def edit_service(request, service_id):

    if request.method == "POST":

        service = get_object_or_404(Service, pk=int(service_id))
        form = EditService(request.POST, instance=service)

        if form.is_valid():
            object_Service = form.save(commit=False)
            object_Service.company = request.user.company
            object_Service.save()

            response_data = {}
            response_data['result'] = 'true'
            response_data['id'] = object_Service.id
            response_data['name'] = object_Service.name

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

        form = EditService()

#     return render(request,'service_add.html', {'form': form})


def delete_service(request, service_id):

    if request.method == 'POST':

        service = get_object_or_404(Service, pk=service_id)
#         myservices = get_object_or_404(Service, pk=int(QueryDict(request.body).get('service_pk')))
        service.delete()

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


def get_info_service(request, service_id):

    if request.method == 'POST':

        service = get_object_or_404(Service, pk=service_id)
#         myservices = get_object_or_404(Service, pk=int(QueryDict(request.body).get('service_pk')))
        form_edit_service = EditService(instance=service)

        response_data = {}
        response_data.update(csrf(request))
        response_data['form_edit_service'] = form_edit_service

        return HttpResponse(
            render(request, 'service_form_edit.html', response_data))

    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def list_services(request, value_filter = "all"):

    if value_filter == 'all':
        service_list = Service.objects.filter(company=request.user.company)
    elif value_filter == 'active':
        service_list = Service.objects.filter(
            is_active=True,
            company=request.user.company)
    elif value_filter == 'inactive':
        service_list = Service.objects.filter(
            is_active=False,
            company=request.user.company)
    else:
        service_list = Service.objects.filter(
            pk=0,
            company=request.user.company)

    if request.method == "POST":

        response_data = {}
        response_data.update(csrf(request))
        response_data['service_list'] = service_list

        return HttpResponse(
            render(request, 'service_list.html', response_data))

    else:
#                 service_list = Service.objects.filter(mycompanies=request.user.mycompanies)

        return render(request, 'service_index.html', {
            'service_list': service_list,
            'form_list_service': NewService(),
            'form_new_service': NewService(),
            'form_edit_service': EditService(),
        }
        )
        
class ServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer        
