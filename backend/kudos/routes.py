from django.urls import path
from kudos.api.auth import login_view, me_view, get_users_by_org
from kudos.api.kudos import send_kudos_view, get_kudos

urlpatterns = [
    path('api/login', login_view, name='login'),
    path('api/me', me_view, name='me'),
    path('api/users', get_users_by_org),
    path('api/send-kudos', send_kudos_view, name='send_kudos'),
    path('api/get-kudos', get_kudos, name='get_kudos'),
]
