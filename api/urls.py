from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="user"), 
    path('get-messages/<str:conversation_id>', views.get_messages, name="get-messages"),
    path('send-message', views.send_message, name="send-message"),
]