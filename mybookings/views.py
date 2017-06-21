# coding=utf-8
from django.shortcuts import render, get_object_or_404
from mybookings.models import Booking
from django.template.context_processors import csrf
from django.http import HttpResponse
from mybookings.forms import NewBooking
from mybookings.forms import EditBooking
import json
from myusers.models import MyUser
import logging
from django.views.generic.edit import CreateView
from myclients.models import Client
from django.views.generic.list import ListView
from pytz import timezone
import pytz
# import datetime
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from mybookings.serializers import BookingListSerializer
from mybookings.serializers import EventsSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt        
class BookingCreate(CreateView):
    model = Booking
    template_name = "booking_add.html"
    fields = ('date_time', 'myclients', 'myservices', 'myexperts')
    
#     success_url = "/bookings/"
    def get(self, request, *args, **kwargs):
        self.initial["myclients"] = Client.objects.get(pk=5)
        return CreateView.get(self, request, *args, **kwargs)
#         return super(CreateView, self).get(request, *args, **kwargs)
# 
# 
#     def get_context_data(self, **kwargs):
#         context = CreateView.get_context_data(self, **kwargs)
#         context["myclients"] = Client.objects.filter(mycompanies=2)
#         return context

@csrf_exempt 
def add_booking(request):

    if request.method == "POST":

        form = NewBooking(request.POST)

        if form.is_valid():
            try:
                object_booking = form.save(commit=False)
#             try:
#                 object_user = MyUser.objects.get(username=object_booking.phone);
#                 object_booking.user = object_user
#                 object_booking.firstname = object_user.firstname
#                 object_booking.lastname = object_user.lastname
#                 object_booking.middlename = object_user.middlename
#             
            
                object_booking.company = request.user.company
                timezone_company = object_booking.company.timezone
                if timezone_company != 'UTC' and timezone_company != '':
                    local = timezone(timezone_company)
                    date_time_local = object_booking.date_time.replace(tzinfo = None)
                    date_time_local = local.localize(date_time_local)
                    object_booking.date_time = date_time_local.astimezone(pytz.UTC)
                
                object_booking.date = object_booking.date_time.date()
                object_booking.time = object_booking.date_time.time()
                object_booking.save()
            
            except Exception as msg:
                logger = logging.getLogger(__name__)
                logger.exception(msg)

            response_data = {}
            response_data['result'] = 'true'
            response_data['id'] = object_booking.id
            response_data['name'] = str(object_booking)

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
        form = NewBooking()

@csrf_exempt
def edit_booking(request, booking_id):

    if request.method == "POST":

        booking = get_object_or_404(Booking, pk=int(booking_id))
        form = EditBooking(request.POST, instance=booking)

        if form.is_valid():
            object_booking = form.save(commit=False)
            try:
                object_user = MyUser.objects.get(username=object_booking.phone);
                object_booking.user = object_user;

            except Exception as msg:
                object_booking.user = None
                logger = logging.getLogger(__name__)
                logger.exception(msg)
            
            object_booking.company = request.user.company
            object_booking.save()

            response_data = {}
            response_data.update(csrf(request))
            response_data['result'] = 'true'
            response_data['id'] = object_booking.id
            response_data['name'] = object_booking.name

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

        form = EditBooking()
@csrf_exempt
def delete_booking(request, booking_id):

    if request.method == 'POST':

        booking = get_object_or_404(Booking, pk=booking_id)
        booking.delete()

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

@csrf_exempt
def get_info_booking(request, booking_id):

    if request.method == 'POST':

        if booking_id == '0':
            form_edit_booking = NewBooking()
        else:     
            booking = get_object_or_404(Booking, pk=booking_id)
            form_edit_booking = EditBooking(instance=booking)

        response_data = {}
        response_data.update(csrf(request))
        response_data['form_edit_booking'] = form_edit_booking

        return HttpResponse(
            render(request, 'booking_form_edit.html', response_data))

    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

@csrf_exempt
def list_bookings(request, value_filter = "all"):

    if value_filter == 'all':
        bookings_list = Booking.objects.filter(company=request.user.company)
    elif value_filter == 'is_new':
        bookings_list = Booking.objects.filter(is_new=True, company=request.user.company)
    elif value_filter == 'is_not_new':
        bookings_list = Booking.objects.filter(is_new=False, company=request.user.company)
    else:
        bookings_list = Booking.objects.filter(pk=0, company=request.user.company)

    if request.method == "POST":

        response_data = {}
        response_data.update(csrf(request))
        response_data['bookings_list'] = bookings_list

        return HttpResponse(
            render(request, 'bookings_list.html', response_data))

    else:

        return render(request, 'bookings_index.html', {
            'bookings_list': bookings_list,
#             'form_new_booking': NewBooking(),
            'form_edit_booking': EditBooking()
        }
        )

@csrf_exempt        
class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Booking.objects.all().order_by('-date_time')
    serializer_class = BookingListSerializer
    
@csrf_exempt
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
            
@csrf_exempt    
def booking_get_evets(request):
 
    if request.method == 'GET':
        queryset = Booking.objects.all()
        serializer = EventsSerializer(queryset, many = True)   
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EventsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
    
    
@csrf_exempt
def booking_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        obj_booking = Booking.objects.get(pk=pk)
    except Booking.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EventsSerializer(obj_booking)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EventsSerializer(obj_booking, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj_booking.delete()
        return HttpResponse(status=204)

def home(request):
    return render(request, 'websocket.html')

