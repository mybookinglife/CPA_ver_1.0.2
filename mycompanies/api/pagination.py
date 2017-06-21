from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination 

class CompanyLimitOffSetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10
    
class CompanyPageNumberPagination(PageNumberPagination):
    page_size = 10