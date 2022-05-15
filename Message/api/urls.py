from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from .views import *

urlpatterns = [
    path('messages/',MessageRoute.as_view(),name='messages'),
    path('updateMsg/<int:id>/',UpdateMessage.as_view(),name='update'),
    path('auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
]