from rest_framework.permissions import BasePermission

class IsGerenteDeObra(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'gerentedobra')

class IsMestreDeObra(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'mestredeobra')
