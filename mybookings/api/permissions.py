from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwner(BasePermission):
    message = "You must be the owner of this booking"
    my_safe_method = ["GET", "PUT", "POST", "DELETE"]
    
#     def has_permission(self, request, view):
#         if request.method in SAFE_METHODS:
#             return True
#         return False
    
    def has_object_permission(self, request, view, obj):
        if request.method in self.my_safe_method:
            return obj.company == request.user.company or obj.client.user == request.user
        return False  
#         return obj.company == request.user.company