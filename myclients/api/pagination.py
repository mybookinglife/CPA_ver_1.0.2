from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination 

class ClientLimitOffSetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 5
    
class ClientPageNumberPagination(PageNumberPagination):
    page_size = 5