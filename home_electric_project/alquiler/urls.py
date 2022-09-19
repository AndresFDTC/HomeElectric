from django.urls import path
from .views import RegisterTool, ListTool

urlpatterns = [
    path('reg_tool/', RegisterTool.as_view(), name='register_tool'),
    path('list_tool/', ListTool.as_view(), name='list_tool'),
]
