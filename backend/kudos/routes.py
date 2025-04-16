from django.urls import path
from kudos.api.auth import CustomTokenObtainPairView

urlpatterns = [
    path('api/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
