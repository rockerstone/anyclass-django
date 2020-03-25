from rest_framework import permissions


class CreateOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        else:
            return False


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        else:
            return False


class AdminDestoryOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "DELETE":
            return request.user.is_staff
        else:
            return True
