from rest_framework import permissions
from django.contrib.auth.models import Group


class GroupPermission(permissions.BasePermission):
    """
    Permission check for User Group
    """
    group_name = ""

    def has_permission(self, request, view):
        message = "You are not authorized to use this endpoint"
        try:
            group = request.user.groups.get(name=self.group_name)
        except Group.DoesNotExist:
            self.message = message
            return False

        return group.name == self.group_name


class UserGroupPermission(GroupPermission):
    """
    Checks if the user is in Users group
    """

    group_name = "Users"


class MentorGroupPermission(GroupPermission):
    """
    Checks if the user is in Users group
    """

    group_name = "Mentors"
