from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.shortcuts import get_object_or_404
from ngo.models import Ngo


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        print("verified 1")
        return request.method in SAFE_METHODS


class IsAuthenticatedUserNgo(BasePermission):
    def has_permission(self, request, view):
        ngo = get_object_or_404(Ngo, username=request.user.username)
        print("verified 2")
        return ngo.IsNgo


class IsProceedByNgo(BasePermission):
    def has_object_permission(self, request, view, obj):
        ngo = get_object_or_404(Ngo, username=request.user.username)
        print("verified 3")
        return obj.ngo == ngo
