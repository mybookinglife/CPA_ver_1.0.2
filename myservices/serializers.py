from rest_framework import serializers
from myservices.models import Service, TypeService
from mycompanies.serializers import CompanyDetailSerializer

class TypeServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypeService
        fields = ('id', 'name', 'is_active')


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    
    type_service = TypeServiceSerializer()
    company = CompanyDetailSerializer()
    
    class Meta:
        model = Service
        fields = ('id','name', 'is_active', 'type_service', 'company', 'number_of_experts', 'price', 'duration')
        

class ShortServiceSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Service
        fields = ('id','name')        