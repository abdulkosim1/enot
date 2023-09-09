from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwner(BasePermission):

    def has_permission(self, request, view): # GET POST
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_owner and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj): # GET by id, PUT PATCH DELETE
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.owner and request.user.is_authenticated 

