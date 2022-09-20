from django.urls import path
from .views import RegisterTool, ListTool, RetrieveTool, UpdateTool, DeleteTool

urlpatterns = [
    path('reg_tool/', RegisterTool.as_view(), name='register_tool'),
    path('list_tool/', ListTool.as_view(), name='list_tool'),
    path('retrieve_tool/<pk>', RetrieveTool.as_view(), name='retrieve_tool'),
    path('update_tool/<pk>', UpdateTool.as_view(), name='update_tool'),
    path('delete_tool/<pk>', DeleteTool.as_view(), name='delete_tool'),
]
