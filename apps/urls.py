from django.urls import path, include

urlpatterns = [
    # Users
    path('auth/', include('apps.users.urls')),

    # Employment
    path('', include('apps.employment.urls')),

    # Orders
    path('', include('apps.orders.urls'))
]
