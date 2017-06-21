from rest_framework import serializers
from mybookings.models import Booking
from myclients.serializers import ShortClientSerializer
from myservices.serializers import ShortServiceSerializer
from myexperts.serializers import ShortExpertSerializer
from pytz import timezone
import datetime
from mycompanies.serializers import CompanyDetailSerializer

# class BookingSerializer(serializers.HyperlinkedModelSerializer):
class BookingListSerializer(serializers.ModelSerializer):
    
#     company = ShortCompanySerializer()
#     client = ShortClientSerializer()
#     service = ShortServiceSerializer()
#     expert = ShortExpertSerializer()
    url = serializers.HyperlinkedIdentityField(
        view_name='api-mybooking:detail',
        lookup_field = "pk"
        )
    phone = serializers.SerializerMethodField()
    client = serializers.SerializerMethodField()
    service = serializers.SerializerMethodField()
    expert = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        
        fields = ('url','id','date_time', 'date', 'time', 'company', 'client', 'phone', 'service', 'expert', 'is_new', 'is_cansel', 'is_finished')
#         fields = ('id','date_time', 'date', 'time', 'note', 'comment', 'is_new', 'is_cansel', 'is_finished')

    def get_phone(self, obj):
        return obj.client.phone

    def get_client(self, obj):
        return obj.client.name

    def get_service(self, obj):
        return obj.service.name

    def get_expert(self, obj):
        return obj.expert.name


class BookingDetailSerializer(serializers.ModelSerializer):
    
    # company = CompanyDetailSerializer()
    # client = ShortClientSerializer()
    # service = ShortServiceSerializer()
    # expert = ShortExpertSerializer()
    
    class Meta:
        model = Booking
        
        fields = ('id', 'date_time', 'date', 'time', 'company', 'client', 'service', 'expert', 'note', 'comment', 'is_new', 'is_cansel', 'is_finished')
#         fields = ('id','date_time', 'date', 'time', 'note', 'comment', 'is_new', 'is_cansel', 'is_finished')


class BookingCreateUpdateSerializer(serializers.ModelSerializer):
    
#     company = ShortCompanySerializer()
#     client = ShortClientSerializer()
#     service = ShortServiceSerializer()
#     expert = ShortExpertSerializer()
    
    class Meta:
        model = Booking
        
        fields = ('id', 'date_time', 'date', 'time', 'company', 'client', 'service', 'expert', 'note', 'comment', 'is_new', 'is_cansel', 'is_finished')
#         fields = ('id','date_time', 'date', 'time', 'note', 'comment', 'is_new', 'is_cansel', 'is_finished')


class EventsSerializer(serializers.ModelSerializer):
    
    title = serializers.SerializerMethodField()
    start = serializers.SerializerMethodField()
    end = serializers.SerializerMethodField()
    
    class Meta:
        model = Booking
        fields = ('id', 'title', 'start', 'end', )
        
    def get_start(self, obj):
        return obj.date_time.astimezone(timezone(obj.company.timezone)).strftime("%Y-%m-%dT%H:%M")
     
    def get_end(self, obj):
        delta = datetime.timedelta(hours=2)
        end_date = obj.date_time.astimezone(timezone(obj.company.timezone)) + delta
        return end_date.strftime("%Y-%m-%dT%H:%M")  
     
    def get_title(self, obj):
        return 'Booking №'+ str(obj.id)     