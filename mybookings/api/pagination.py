from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination 

class BookingLimitOffSetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10
    
class BookingPageNumberPagination(PageNumberPagination):
    page_size = 100