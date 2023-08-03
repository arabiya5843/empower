from django.urls import path

from apps.orders.views import UserCardListCreateAPIView, UserCardDestroyAPIView

urlpatterns = [
    # User Cards List and Create View
    path('user-cards/', UserCardListCreateAPIView.as_view(), name='user-card-list'),

    # User Card Destroy View
    path('user-cards/<int:pk>/', UserCardDestroyAPIView.as_view(),
         name='user-card-destroy'),
]
