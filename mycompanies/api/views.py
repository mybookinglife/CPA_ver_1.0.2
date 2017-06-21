from django.db.models import Q
from rest_framework.generics import( 
    ListAPIView, 
    RetrieveAPIView, 
    UpdateAPIView, 
    DestroyAPIView, 
    CreateAPIView)

from mycompanies.models import Company, Activity
from mycompanies.serializers import (
    ActivitySerializer,
    CompanyListSerializer, 
    CompanyDetailSerializer, 
    CompanyCreateUpdateSerializer, 
    )
from .permissions import IsOwner
from .pagination import CompanyPageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

# from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

class CompanyCreateApiView(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyCreateUpdateSerializer 
    permission_classes = [IsAuthenticated, IsOwner]
    
    def perform_create(self, serializer):
        serializer.save()  


class CompanyUpdateApiView(UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyCreateUpdateSerializer 
    permission_classes = [IsAuthenticated, IsOwner]
    
    def perform_update(self, serializer):
        serializer.save()  
        
    
class CompanyDeleteApiView(DestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyListSerializer
    permission_classes = [IsAuthenticated, IsOwner] 


class CompanyDetailApiView(RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    

class CompanyListApiView(ListAPIView):
    serializer_class = CompanyListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "phone", "legalname", "actual_adress"]
    pagination_class = CompanyPageNumberPagination#PageNumberPagination
    
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self, *args, **kwargs):
#         queryset_list = super(BookingListApiView, self).get_queryset(*args, **kwargs)
#         queryset_list = Booking.objects.filter(company = self.request.user.company)
        queryset_list = Company.objects.filter()
        is_active = self.request.GET.get("is_active")
        if is_active:
            queryset_list = queryset_list.filter(is_active=is_active)
  
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains = query)|
                Q(phone__icontains = query)|
                Q(legalname__icontains = query)|
                Q(actual_adress__icontains = query)

                ).distinct()
        
        return queryset_list    

class ActivityListApiView(ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    pagination_class = CompanyPageNumberPagination#PageNumberPagination
    permission_classes = [IsAuthenticated]