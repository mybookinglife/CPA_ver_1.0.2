from django.shortcuts import render, get_object_or_404
from myexperts.models import Expert
from myexperts.models import Service_Experts
from myservices.models import Service
from django.template.context_processors import csrf
from myexperts.forms import NewExpert
from myexperts.forms import EditExpert
from django.http import HttpResponse
import json
import logging
from django.core.mail import send_mail
from rest_framework import viewsets
from myexperts.serializers import ExpertSerializer


# Create your views here.
def add_expert(request):

    if request.method == "POST":

        form = NewExpert(request.POST)

        if form.is_valid():
            object_Expert = form.save(commit=False)
#             Service.is_active = False
            object_Expert.company = request.user.company
            object_Expert.save()

            response_data = {}
            response_data['result'] = 'true'
            response_data['id'] = object_Expert.id
            response_data['name'] = object_Expert.name

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
        form = NewExpert()


def edit_expert(request, expert_id):

    if request.method == "POST":

        expert = get_object_or_404(Expert, pk=int(expert_id))
        form = EditExpert(request.POST, instance=expert)

        if form.is_valid():
            object_Expert = form.save(commit=False)
            object_Expert.company = request.user.company
            object_Expert.save()

            response_data = {}
            response_data['result'] = 'true'
            response_data['id'] = object_Expert.id
            response_data['name'] = object_Expert.name

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

        form = EditExpert()


def delete_expert(request, expert_id):

    if request.method == 'POST':

        object_Expert = get_object_or_404(Expert, pk=expert_id)
#         myservices = get_object_or_404(Service, pk=int(QueryDict(request.body).get('service_pk')))
        object_Expert.delete()

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


def get_info_expert(request, expert_id):

    if request.method == 'POST':

        expert = get_object_or_404(Expert, pk=expert_id)
#         myservices = get_object_or_404(Service, pk=int(QueryDict(request.body).get('service_pk')))
        form_edit_expert = EditExpert(instance=expert)

        response_data = {}
        response_data.update(csrf(request))
        response_data['form_edit_expert'] = form_edit_expert

        return HttpResponse(
            render(request, 'expert_form_edit.html', response_data))

    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def list_expert(request, value_filter="all"):

    if value_filter == 'all':
        expert_list = Expert.objects.filter(company=request.user.company)
    elif value_filter == 'active':
        expert_list = Expert.objects.filter(
            is_active=True,
            company=request.user.company)
    elif value_filter == 'inactive':
        expert_list = Expert.objects.filter(
            is_active=False,
            company=request.user.company)
    else:
        expert_list = Expert.objects.filter(pk=0, company=request.user.company)

    if request.method == "POST":

        response_data = {}
        response_data.update(csrf(request))
        response_data['expert_list'] = expert_list

        return HttpResponse(render(request, 'expert_list.html', response_data))

    else:
        #         service_list = Service.objects.filter(mycompanies=request.user.mycompanies)

        return render(request, 'expert_index.html', {
            'expert_list': expert_list,
            'form_list_expert': NewExpert(),
            'form_new_expert': NewExpert(),
            'form_edit_expert': EditExpert()
        }
        )


def add_service_experts(request, expert_id, service_id):

    #     if request.method == "POST":

    try:
        object_expert = Expert.objects.get(pk=expert_id)
        object_service = Service.objects.get(pk=service_id)
        object_Service_Experts, created = Service_Experts.objects.get_or_create(
            expert=object_expert, service=object_service)
#
        response_data = {}
        response_data['result'] = 'true'
        response_data['id'] = object_Service_Experts.id
        response_data['created'] = created

    except Exception as msg:

        logger = logging.getLogger(__name__)
        logger.exception(msg)

        response_data = {}
        response_data['result'] = 'false'

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )

#     else:
#         return HttpResponse(
#             json.dumps({"nothing to see": "this isn't happening"}),
#             content_type="application/json"
#         )


def delete_service_experts(request, expert_id, service_id):

    if request.method == 'POST':
        try:
            object_expert = Expert.objects.get(pk=expert_id)
            object_service = Service.objects.get(pk=service_id)
            object_Service_Experts = Service_Experts.objects.get(
                expert=object_expert,
                service=object_service)
#             myservices = get_object_or_404(Service, pk=int(QueryDict(request.body).get('service_pk')))
            object_Service_Experts.delete()

            response_data = {}
            response_data['result'] = 'true'
        except Exception as msg:

            logger = logging.getLogger(__name__)
            logger.exception(msg)

            response_data = {}
            response_data['result'] = 'false'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def get_service_experts(request, expert_id):

    if request.method == 'POST':

  
        try:
    
            text_query = """SELECT T1.id,
            IFNULL(T2.is_active, 0) is_active,
            """+str(expert_id)+""" expert_id
            FROM services T1
            LEFT JOIN services_experts T2
            ON T1.id = T2.service_id AND T2.expert_id = """+str(expert_id)+"""
            WHERE T1.is_active = 1
            AND T1.company_id = """+str(request.user.company_id)
            
    
            object_service = Service.objects.raw(text_query)
    
            response_data = {}
            response_data.update(csrf(request))
            response_data['service_experts_list'] = object_service
    
        except Exception as msg:
    
            logger = logging.getLogger(__name__)
            logger.exception(msg)
    
        return HttpResponse(render(request, 'service_experts_list.html', response_data))

    else:
        
        response_data = {}
        response_data.update(csrf(request))
        response_data['service_experts_list'] = object_service
        
        return HttpResponse(render(request, 'service_experts_list.html', response_data))


class ExpertViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer


def sendmail(request):

    send_mail('Subject here', 'Here is the message.', 'my.mybookings.myservices@gmail.com',
              ['bssoft.ks@mail.ru'], fail_silently=False)

    return HttpResponse("Отправили тестовое письмо")
