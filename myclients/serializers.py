from rest_framework import serializers
from myclients.models import Client
from mycompanies.serializers import CompanyDetailSerializer

class ClientListSerializer(serializers.ModelSerializer):
    
    url = serializers.HyperlinkedIdentityField(
        view_name = 'api-myclients:detail',
        lookup_field = 'pk'
        )
    
    class Meta:
        model = Client
        fields = ('url', 'id', 'name', 'phone', 'email', 'is_vip', 'company')


class ClientDetailSerializer(serializers.ModelSerializer):
    
    company = CompanyDetailSerializer()
    
    class Meta:
        model = Client
        fields = ('id', 'name', 'phone', 'firstname', 'lastname', 'middlename', 'email', 'is_vip', 'note', 'company')
        

class ClientCreateUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = ('id', 'name', 'phone', 'firstname', 'lastname', 'middlename', 'email', 'is_vip', 'note', 'company')


        
class ShortClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = ('id', 'name', 'phone')