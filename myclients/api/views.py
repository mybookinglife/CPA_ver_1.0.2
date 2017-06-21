from django.db.models import Q
from rest_framework.generics import( 
    ListAPIView, 
    RetrieveAPIView, 
    UpdateAPIView, 
    DestroyAPIView, 
    CreateAPIView)
from myclients.models import Client
from myclients.serializers import (
    ClientListSerializer, 
    ClientDetailSerializer, 
    ClientCreateUpdateSerializer, 
    )
from .permissions import IsOwner
from .pagination import ClientPageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

# from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

class ClientCreateApiView(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientCreateUpdateSerializer 
    permission_classes = [IsAuthenticated, IsOwner]
    
    def perform_create(self, serializer):
        serializer.save()  


class ClientUpdateApiView(UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientCreateUpdateSerializer 
    permission_classes = [IsAuthenticated, IsOwner]
    
    def perform_update(self, serializer):
        serializer.save()  
        
    
class ClientDeleteApiView(DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientListSerializer
    permission_classes = [IsAuthenticated, IsOwner] 


class ClientDetailApiView(RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    

class ClientListApiView(ListAPIView):
    serializer_class = ClientListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "phone", "firstname", "lastname", "middlename", "email"]
    pagination_class = ClientPageNumberPagination#PageNumberPagination
    
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self, *args, **kwargs):
#         queryset_list = super(BookingListApiView, self).get_queryset(*args, **kwargs)
#         queryset_list = Booking.objects.filter(company = self.request.user.company)
        queryset_list = Client.objects.filter(company=self.request.user.company)
        is_vip = self.request.GET.get("is_vip")
        if is_vip:
            queryset_list = queryset_list.filter(is_vip=is_vip)
  
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains = query)|
                Q(phone__icontains = query)|
                Q(firstname__icontains = query)|
                Q(lastname__icontains = query)|
                Q(middlename__icontains = query)|
                Q(email__icontains = query)|
                Q(note__icontains = query)
                ).distinct()
        
        return queryset_list    
        