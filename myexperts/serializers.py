from rest_framework import serializers
from myexperts.models import Expert
from mycompanies.serializers import CompanyDetailSerializer

class ExpertSerializer(serializers.HyperlinkedModelSerializer):
    
    company = CompanyDetailSerializer()
    
    class Meta:
        model = Expert
        fields = ('id','name', 'phone', 'company', 'short_description', 'description', 'is_active')
        
        
class ShortExpertSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Expert
        fields = ('id','name')