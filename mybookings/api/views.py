from django.db.models import Q
from rest_framework.generics import(
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListCreateAPIView,
    CreateAPIView)

from mybookings.models import Booking
from mybookings.serializers import (
    BookingListSerializer,
    BookingDetailSerializer,
    BookingCreateUpdateSerializer,
    )
from .permissions import IsOwner
from .pagination import BookingPageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework import status


# from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

class BookingCreateApiView(CreateAPIView):
    # queryset = Booking.objects.all()
    serializer_class = BookingCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(is_new=True)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #
    #     serializer_response = BookingListSerializer(Booking.objects.filter(id=serializer.data.get("id")))
    #
    #     headers = self.get_success_headers(serializer_response.data)
    #     return Response(serializer_response.data, status=status.HTTP_201_CREATED, headers=headers)


class BookingUpdateApiView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def perform_update(self, serializer):
        serializer.save()


class BookingDeleteApiView(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class BookingDetailApiView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
    permission_classes = [IsAuthenticated, IsOwner]

class BookingListApiView(ListAPIView):
    serializer_class = BookingListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["date_time", "client__name", "expert__name", "service__name"]
    pagination_class = BookingPageNumberPagination#PageNumberPagination

    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
#         queryset_list = super(BookingListApiView, self).get_queryset(*args, **kwargs)
#         queryset_list = Booking.objects.filter(company = self.request.user.company)
        queryset_list = Booking.objects.filter(company=self.request.user.company)
        is_new = self.request.GET.get("is_new")
        if is_new:
            queryset_list = queryset_list.filter(is_new=is_new)
        is_finish = self.request.GET.get("is_finish")
        if is_finish:
            queryset_list = queryset_list.filter(is_finish=is_finish)
        is_cancel = self.request.GET.get("is_cancel")
        if is_cancel:
            queryset_list = queryset_list.filter(is_cansel=is_cancel)

        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(date_time__icontains = query)|
                Q(client__name__icontains = query)|
                Q(expert__name__icontains = query)|
                Q(service__name__icontains = query)|
                Q(note__icontains = query)|
                Q(comment__icontains = query)
                ).distinct()

        return queryset_list
