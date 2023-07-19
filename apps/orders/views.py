from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.orders.models import UserCard
from apps.orders.permissions import IsOwnerOfCard
from apps.orders.serializers import UserCardSerializer


# View for listing and creating user cards
class UserCardListCreateAPIView(ListCreateAPIView):
    serializer_class = UserCardSerializer
    permission_classes = (IsAuthenticated, IsOwnerOfCard)

    # Get the queryset for the user's cards
    def get_queryset(self):
        return UserCard.objects.filter(user_id=self.request.user.pk)

    # Save the current user as the owner of the card when creating
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# View for deleting a user card
class UserCardDestroyAPIView(DestroyAPIView):
    serializer_class = UserCardSerializer
    permission_classes = (IsAuthenticated, IsOwnerOfCard)

    # Get the queryset for the user's cards
    def get_queryset(self):
        return UserCard.objects.filter(user_id=self.request.user.pk)
