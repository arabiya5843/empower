from rest_framework.permissions import BasePermission


# Custom permission class to check if the requesting user is the owner of a card
class IsOwnerOfCard(BasePermission):

    # Method to check object-level permission
    def has_object_permission(self, request, view, obj):
        # Compare the user associated with the card object (obj) with the requesting user (request.user)
        # If they are the same, the requesting user is the owner of the card and has permission
        return obj.user == request.user
