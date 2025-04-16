from django.urls import path
from kudos.api.auth import login_view, me_view
from kudos.api.kudos import send_kudos_view

urlpatterns = [
    path('api/login/', login_view, name='login'),
    path('api/me/', me_view, name='me'),
    path('api/send-kudos/', send_kudos_view, name='send_kudos'),
]
