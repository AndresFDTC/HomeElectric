from django.urls import path
from .views import RegisterView, RegisterList
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('registro/', RegisterView.as_view(), name='register_view'),
    path('lista/', RegisterList.as_view(), name='register_list'),
]
