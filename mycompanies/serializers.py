from rest_framework import serializers
from mycompanies.models import Company, Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'name', 'is_active')

class CompanyListSerializer(serializers.ModelSerializer):
    
    url = serializers.HyperlinkedIdentityField(
            view_name='api-mycompanies:detail',
            lookup_field = "pk"
            )
        
    class Meta:
        model = Company
        fields = ('url', 'id', 'name', 'is_active', 'legal_name', 'itn', 'phone', 'legal_address')

class CompanyDetailSerializer(serializers.ModelSerializer):
    
    activity = ActivitySerializer()
    
    class Meta:
        model = Company
        fields = ('id', 'name', 'is_active', 'legal_name', 'itn', 'phone', 'legal_address', 'actual_address', 'activity', 'language', 'timezone')
        
class CompanyCreateUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = ('id', 'name', 'is_active', 'legal_name', 'itn', 'phone', 'legal_address', 'actual_address', 'activity', 'language', 'timezone')
        
