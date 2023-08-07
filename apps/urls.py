from django.urls import path, include

urlpatterns = [
    # AI Your Supportive
    path('ai/', include('apps.ai_supportive.urls')),

    # Users
    path('auth/', include('apps.users.urls')),

    # Employment
    path('', include('apps.employment.urls')),

    # Orders
    path('', include('apps.orders.urls'))
]