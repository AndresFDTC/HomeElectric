from django.urls import path
from .views import *

urlpatterns = [
    path('reg_tool/', RegisterTool.as_view(), name='register_tool'),
    path('list_tool/', ListTool.as_view(), name='list_tool'),
    path('retrieve_tool/<int:pk>', RetrieveTool.as_view(), name='retrieve_tool'),
    path('update_tool/<int:pk>', UpdateTool.as_view(), name='update_tool'),
    path('delete_tool/<int:pk>', DeleteTool.as_view(), name='delete_tool'),
    path('reg_rent/', RegisterRent.as_view(), name='register_rent'),
    path('list_rent/', ListRent.as_view(), name='list_rent'),
    path('retrieve_rent/<int:pk>', RetrieveRent.as_view(), name='retrieve_rent'),
    path('update_rent/<int:pk>', UpdateRent.as_view(), name='update_rent'),
    path('delete_rent/<int:pk>', DeleteRent.as_view(), name='delete_rent'),
    path('rents_user/<int:usuario_id>', RentsByUser.as_view(), name='rents_user'),
    path('tool_name/<str:nombre>', RetrieveToolForMenu.as_view(), name ='tool_name'),
]
